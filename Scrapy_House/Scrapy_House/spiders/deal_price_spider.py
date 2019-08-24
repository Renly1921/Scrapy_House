import scrapy
from Scrapy_House.items import DealPriceItem

class Spider(scrapy.Spider):
    name = "deal_price"
    allowed_domains = ["hz.ke.com"]
    region_input = ["松木场河东"]

    start_urls = ["https://hz.5i5j.com/sold/100000000003563/"]
#                  "https://hz.ke.com/ershoufang/a2a3rs檀香园/",
#                  "https://hz.ke.com/ershoufang/a2a3rs天安假日公寓/",
#                  "https://hz.ke.com/ershoufang/a2a3rs建国公寓/"]

    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 1,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'user_trace_token=20171015132411-12af3b52-3a51-466f-bfae-a98fc96b4f90; LGUID=20171015132412-13eaf40f-b169-11e7-960b-525400f775ce; SEARCH_ID=070e82cdbbc04cc8b97710c2c0159ce1; ab_test_random_num=0; X_HTTP_TOKEN=d1cf855aacf760c3965ee017e0d3eb96; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DsXIrWUxpNGLE2g_bKzlUCXPTRJMHxfCs6L20RqgCpUq%26wd%3D%26eqid%3Dee53adaf00026e940000000559e354cc; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_hotjob; login=false; unick=""; _putrc=""; JSESSIONID=ABAAABAAAFCAAEG50060B788C4EED616EB9D1BF30380575; _gat=1; _ga=GA1.2.471681568.1508045060; LGSID=20171015203008-94e1afa5-b1a4-11e7-9788-525400f775ce; LGRID=20171015204552-c792b887-b1a6-11e7-9788-525400f775ce',
            'Host': 'hz.5i5j.com',
            'Origin': 'https://hz.5i5j.com',
            'Referer': 'https://hz.5i5j.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }

    def parse(self, response):
        houses = response.css('listCon')
        for house in houses:
            item = DealPriceItem()
#            item['deal_id'] = house.css('a::attr(href)').extract_first()[6:14] + '\t'   # 加\t以便CSV打开的时候不会变成科学计数法
            item['deal_title'] = str(house.css('.sTit strong::text').extract_first()[1]) + str(house.css('.listCon .sTit strong::text').extract_first()[2])
            item['deal_info'] = house.css('p::text').extract()[2]
            item['deal_date'] = str(house.css('p::text').extract()[3])
            item['deal_price'] = house.css('.jiage strong::text').extract_first() + '万'
            item['deal_average'] = house.css('.jiage p::text').extract_first()
            # 数据清洗，去空格，去换行，并合并成一个字符串
#            item['house_info'] = [x.strip() for x in item['house_info'] if x.strip() != '']
#            xx = ''
#            for x in item['house_info']:
#               xx += x
#            item['house_info'] = xx
            print(item)
            yield item





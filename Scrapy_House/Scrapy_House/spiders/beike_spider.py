import scrapy
from Scrapy_House.items import ScrapyHouseItem

class Spider(scrapy.Spider):
    name = "Beike"
    allowed_domains = ["hz.ke.com"]
    region_input = ["宝善公寓",
                    "檀香园",
                    "天安假日公寓",
                    "建国公寓",
                    "凤起都市花园",
                    "国都公寓",
                    "松木场河东"]
    start_urls = []
    for region in region_input:
        start_urls.append("https://hz.ke.com/ershoufang/a2a3rs" + region + "/;")

#    start_urls = ["https://hz.ke.com/ershoufang/a2a3rs宝善公寓/",
#                  "https://hz.ke.com/ershoufang/a2a3rs檀香园/",
#                  "https://hz.ke.com/ershoufang/a2a3rs天安假日公寓/",
#                  "https://hz.ke.com/ershoufang/a2a3rs建国公寓/"]

    def parse(self, response):
        result_tag = response.css('.resultDes .total span::text').extract_first()
        print(result_tag)
        if result_tag == " 0 ":
            print('该小区没有发现相关房源')
        else:
            houses = response.css('.info')
            for house in houses:
                item = ScrapyHouseItem()
                item['house_title'] = house.css('.title a::attr(title)').extract_first()
                item['house_link'] = house.css('.title a::attr(href)').extract_first()
                item['house_region'] = house.css('.address .flood a::text').extract_first()
                item['house_info'] = str(house.css('.address .houseInfo::text').extract()[1])
                item['house_price'] = house.css('.address .priceInfo .totalPrice span::text').extract_first() + '万'
                item['house_id'] = house.css('.address .priceInfo div::attr(data-hid)').extract_first() + '\t'   # 加\t以便CSV打开的时候不会变成科学计数法
                # 数据清洗，去空格，去换行，并合并成一个字符串
                item['house_info'] = [x.strip() for x in item['house_info'] if x.strip() != '']
                xx = ''
                for x in item['house_info']:
                   xx += x
                item['house_info'] = xx
#                print(item)
                yield item





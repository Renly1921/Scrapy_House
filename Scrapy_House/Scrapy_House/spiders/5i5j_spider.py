import scrapy
from Scrapy_House.items import ScrapyHouseItem

class Spider(scrapy.Spider):
    name = "5i5j"
    allowed_domains = ["hz.5i5j.com"]
    region_input = ["宝善公寓",
                    "檀香园",
                    "天安假日公寓",
                    "建国公寓",
                    "凤起都市花园",
                    "国都公寓",
                    "松木场河东"]
    start_urls = []
    for region in region_input:
        start_urls.append("https://hz.5i5j.com/ershoufang/ershoufang/a2a3/_" + region + "/;")

    def parse(self, response):
        result_tag = response.css('.total-box span::text').extract_first()
        print(result_tag)
        if result_tag == "0":
            print('该小区没有发现相关房源')
        else:
            houses = response.css('.listCon')
            for house in houses[:int(result_tag)]:
                item = ScrapyHouseItem()
                item['house_title'] = house.css('.listTit a::text').extract_first()
                item['house_link'] = "https://hz.5i5j.com" + house.css('.listTit a::attr(href)').extract_first()
                item['house_region'] = house.css('.listX a::text').extract_first()
                item['house_info'] = house.css('.listX p::text').extract_first()
                item['house_price'] = house.css('.listX .jia .redC strong::text').extract_first() + '万'
                item['house_id'] = house.css('.listTit a::attr(href)').extract_first()[12:20]
                # 数据清洗，去空格，去换行，并合并成一个字符串
#                item['house_info'] = [x.strip() for x in item['house_info'] if x.strip() != '']
#                xx = ''
#                for x in item['house_info']:
#                    xx += x
#                item['house_info'] = xx
                print(item)
                yield item

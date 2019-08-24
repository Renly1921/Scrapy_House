import scrapy
from Scrapy_House.items import ScrapyHouseItem

class DemoSpider(scrapy.Spider):
    name = "Demo"
    allowed_domains = ["hz.ke.com"]
    start_urls = ["https://hz.ke.com/ershoufang/a2a3rs%E5%AE%9D%E5%96%84%E5%85%AC%E5%AF%93/"]

    def parse(self, response):
        houses = response.css('.info')
#        print(houses)
        for house in houses:
            ScrapyHouseItem()
            house_title = house.css('.title a::attr(title)').extract_first()
            house_link = house.css('.title a::attr(href)').extract_first()
            house_info = house.css('.address .houseInfo::text').extract()[1]
            house_price = house.css('.address .priceInfo .totalPrice span::text').extract_first()
            house_id = house.css('.address .priceInfo div::attr(data-hid)').extract_first()
            print(house_title)
            print(house_link)
            print(house_info)
            print(house_id)
            print(house_price)
#            yield item





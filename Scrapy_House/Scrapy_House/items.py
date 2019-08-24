# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_title = scrapy.Field()
    house_id = scrapy.Field()
    house_region = scrapy.Field()
    house_info = scrapy.Field()
    house_price = scrapy.Field()
    house_link = scrapy.Field()

class DealPriceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    deal_id = scrapy.Field()
    deal_title = scrapy.Field()
    deal_info = scrapy.Field()
    deal_date = scrapy.Field()
    deal_price = scrapy.Field()
    deal_average = scrapy.Field()
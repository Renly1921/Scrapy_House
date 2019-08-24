# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import CsvItemExporter

class ScrapyHousePipeline(object):
    def open_spider(self, spider):
        self.file = open("house_list.csv", "wb")
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ["house_id", "house_title"]
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print("保存数据成功")
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
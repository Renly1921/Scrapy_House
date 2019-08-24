# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv
import codecs
from scrapy.exporters import CsvItemExporter
import pandas as pd

class ScrapyHousePipeline_find_new(object):

    old_house_id_list = []
    old_info_file = []
    new_info_file = []

    def open_spider(self, spider):
        # 处理记录文件的文件名
        old_info_file = spider.name + "_house_list.csv"
        new_info_file = spider.name + "_new_house_list.csv"

        # 读入原记录文件的房屋编号信息
        try:
            old_data = pd.read_csv(old_info_file)
            self.old_house_id_list = list(old_data['house_id'].astype('str'))
#            self.old_house_id_list = list(old_data.house_id)
        except:
            self.old_house_id_list = []
        print(self.old_house_id_list)

        # 初始化处理csv文件的BOM头
        try:
            f = open(old_info_file, "wb")
            f.write(b'\xef\xbb\xbf')
            f.close()
        except:
            print("增加" + old_info_file + "文件BOM头失败")

        try:
            f = open(new_info_file, "wb")
            f.write(b'\xef\xbb\xbf')
            f.close()
        except:
            print("增加" + new_info_file + "文件BOM头失败")

        # 打开原记录文件，进入可读写状态
        try:
            self.file = open(old_info_file, "ab")
        except:
            print("打开" + old_info_file + "文件失败")
            return
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ["house_id", "house_region", "house_title", "house_price", "house_info", "house_link"]
        self.exporter.start_exporting()

        # 打开新记录文件，进入可读写状态
        try:
            self.newfile = open(new_info_file, "a+", encoding="utf-8", newline='')
            self.writer = csv.writer(self.newfile)
            self.writer.writerow(["house_id", "house_region", "house_title", "house_price", "house_info", "house_link"])
        except:
            print("打开" + new_info_file + "文件失败")
            return



    def process_item(self, item, spider):
        if item['house_id'] not in self.old_house_id_list:
            print("发现新数据  " + item['house_id'] + item['house_title'])
            self.writer.writerow([item['house_id'], item['house_region'], item['house_title'], item['house_price'], item['house_info'], item['house_link']])
        self.exporter.export_item(item)
        print("保存数据成功")
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        self.newfile.close()

#        self.file = codecs.open('house_list.csv', 'ab+', 'utf_8_sig')
#        codecs.
#        self.file.close()

#        with codecs.open("house_list.csv", "wb", "utf-8") as fr:
#            for line in fr:
#                if line[0] == codecs.BOM_UTF8.decode("utf-8"):
#                    line = line[1:]
#            fr.write(line)
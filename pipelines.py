# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pymysql
from scrapy import exporters
from ArticleSpider.items import WzvtcItem
from scrapy.exporters import JsonItemExporter
from ArticleSpider.settings import *

class WzvtcSpiderPipelines(object):

    # 自定义json文件的导出
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item



class WzvtcMysqlPipelines(object):

    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', '123', 'Article_spider', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()


    def process_item(self,item,spider):

        # print(type(item['url']),type(item['title']),type(item['auth']),type(item['create_date']),type(item['content_url']))

        insert_sql = """
                   insert into Wzvtc_spider(title, url, auth,content_url,create_date)
                   VALUES (%s, %s, %s, %s,%s)
               """

        self.cursor.execute(insert_sql,(item['title'],item['url'],item['auth'],item['content_url'],item['create_date']))
        self.conn.commit()

    def close_spider(self,spider):

        self.conn.close()
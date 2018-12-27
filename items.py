# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
from scrapy.loader.processors import TakeFirst # 只取取出的第一个值
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join # 列表连接


class WzvtcItem(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    auth = scrapy.Field()
    create_date = scrapy.Field()
    content_url = scrapy.Field()




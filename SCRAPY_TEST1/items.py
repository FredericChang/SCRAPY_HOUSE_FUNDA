# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader
import datetime
from w3lib.html import remove_tags

class ScrapyTest1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FUNDAITEM(scrapy.Item):
    location1 = scrapy.Field()
    location2 = scrapy.Field()
    price = scrapy.Field()
    bouwjaar = scrapy.Field()
    wonen = scrapy.Field()
    aantak_kamers = scrapy.Field()
    perceel = scrapy.Field()

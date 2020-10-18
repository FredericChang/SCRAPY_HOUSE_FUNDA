# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from SCRAPY_TEST1.items import FUNDAITEM
# class FandaSpider(CrawlSpider):
class FandaSpider(scrapy.Spider):
    name = "FUNDA2"
    allowed_domains = ["www.funda.nl"]
    start_urls = ['https://www.funda.nl/koop/ede/']
    # 下載URL


    def __init__(self, board='FUNDA'):
         self.board = board
         super().__init__()

    def parse_item(self, response):
        x = response.url
        xz = x.split( '/' )
        if len(xz) > 7:
            print("end scrapy this website" + response.url)
            return

        item_loader = ItemLoader(item=FUNDAITEM(), response=response)
        location1 = response.css('.object-header__title::text').extract()[0]
        location2 = response.css('.object-header__subtitle::text').extract()[0]
        price = response.css('.object-header__price::text').extract()[0]
        bouwjaar = response.xpath("// *[ @ id = 'content'] / div / div / div[1] / section[1] / ul / li[1] / span[3]/text()").extract()
        wonen = response.xpath("// *[ @ id = 'content'] / div / div / div[1] / section[1] / ul / li[2] / span[3]/text()").extract()
        aantak_kamers = response.xpath("// *[ @ id = 'content'] / div / div / div[1] / section[1] / ul / li[3] / span[3]/text()").extract()
        perceel = response.xpath("// *[ @ id = 'content'] / div / div / div[1] / section[1] / ul / li[4] / span[3]/text()").extract()

        item_loader.replace_value("location1", location1)
        item_loader.replace_value("location2", location2)
        item_loader.replace_value("price", price)
        item_loader.replace_value("bouwjaar", bouwjaar)
        item_loader.replace_value("wonen", wonen)
        item_loader.replace_value("aantak_kamers", aantak_kamers)
        item_loader.replace_value("perceel", perceel)

        collector_item = item_loader.load_item()
        yield collector_item

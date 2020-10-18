# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from SCRAPY_TEST1.items import FUNDAITEM
class FandaSpider(CrawlSpider):
# class FandaSpider(scrapy.Spider):
    name = "FUNDA"
    allowed_domains = ["www.funda.nl"]
    start_urls = ['https://www.funda.nl/koop/ede/']
    # 下載URL
    # custom_settings = {
    #     "COOKIES_ENABLED": False,
    #     "DOWNLOAD_DELAY": 3,
    #     # 'DEFAULT_REQUEST_HEADERS': {
    #     #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
    #     # }
    # }


    rules = (
        Rule(LinkExtractor(allow=r'/huis-\d{1,8}-\w{1,}-\d{2,}/$'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'/p\d{2}'), follow=True ),
        # Rule( LinkExtractor( allow=r'((?=-\d{1,})-\d{1,}|-\w{1,})/'), callback='parse_item', follow=True ),

    )

    def __init__(self, board='FUNDA'):
         self.board = board
         super().__init__()

    def parse_item(self, response):
        # x = response.url
        # xz = x.split( '/' )
        # if len(xz) > 7:
        #     print("end scrapy this website" + response.url)
        #     return

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
    # def parse(self, response):
    #     if response.status != 200:
    #         print('Error - {} is not available to access'.format(response.url))
    #         return
    #     response.css('.search-result__header-title::text').extract()[0]
    #     response.css('.search-result__header-subtitle::text').extract()[0]
    #     response.css('.search-result-price::text').extract()[0]
    #     response.css('span[title^="Gebruiksoppervlakte wonen"]::text').extract()[0]
    #     response.css('span[title^="Perceeloppervlakte"]::text').extract()[0]
    #     response.css('.search-result-kenmerken > li::text').extract()[0]
    #     a = response.css('.search-result__header-title::text').extract()[0]
    #     pass


# "https://www.funda.nl/koop/ede/huis-41091521-rousseaustate-20/?navigateSource=resultlist"
        # Rule(LinkExtractor(allow=r'^.*\=resultlist$'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'/p\d{2}'), callback='parse_item', follow=True)
        # https: // www.vocabulary.com / lists / mvpp2vfg / hidden-figures

        # ^ (?(?=SI). *  # ¤(?<matchfromend>.+$)$|(?<else>.*))
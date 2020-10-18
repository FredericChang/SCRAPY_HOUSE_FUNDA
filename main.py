import scrapy
import sys
import os
import PIL

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.cmdline import execute


def main():
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    print(sys.path.append(os.path.dirname(os.path.abspath(__file__))))
    # execute(["scrapy", "crawl","iThome"])
    # execute(["scrapy", "crawl","zhihu"])
    execute(["scrapy", "crawl","FUNDA"])
    # target_board = ['NBA']
    # process = CrawlerProcess(get_project_settings())
    # for board in target_board:
    #     # process.crawl('PTTCrawler', board=board)
    #     process.crawl('Shopee', board=board )

    #     process.start()

if __name__ == '__main__':
    main()
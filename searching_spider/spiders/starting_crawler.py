from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from django.db import connection
from multiprocessing import Process
from .all_web_page_spider import AllWebPageSpider
from .only_one_page import OnlyOnePage


class Urls(object):
    url = ''
    base_url = ''

class TransferAsynchron(object):
    robots_txt = ''
    sitemap = ''
    redirect = ''


class BilliardCrawlProcess(Process):

    def run(self):
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl('all_web_page_spider',)
        process.start()

class BilliardCrawlProcessOnePages(Process):

    def run(self):
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl('only_one_page',)
        process.start()

def transfer_url(url,short_url):
    urls=Urls
    urls.url=url
    urls.base_url = short_url




def crawl(url,short_url):
    urls = AllWebPageSpider()
    urls.get_url(url,short_url)
    crawl_process = BilliardCrawlProcess()

    crawl_process.start()
    crawl_process.join()  # blocks here until scrapy finished
    connection.close()
    # NOTE

def crawl_one_pages(url, short_url):
    urls = OnlyOnePage()
    urls.get_url(url, short_url)
    crawl_process = BilliardCrawlProcessOnePages()

    crawl_process.start()
    crawl_process.join()
    connection.close()
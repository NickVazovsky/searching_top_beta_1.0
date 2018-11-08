# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerRunner
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule
from searching_spider.check_seo import Check, Links
from searching_spider.items import SearchingSpiderItem


Ch = Check()
Li = Links()


class AllWebPageSpider(CrawlSpider):
    name = "all_web_page_spider"
    handle_httpstatus_list = [404, 500]
    start_urls = ["https://dulevo.ru"]
    allowed_domains = ["mail.ru"]
    url = ''
    rules = (
        Rule(LinkExtractor(allow=url), callback='parse_asd'),
        Rule(LinkExtractor(allow=url), follow=True),
    )

    def parse_asd(self, response):
        item = SearchingSpiderItem()
        for quote in response.css('html'):
            counters_anal = quote.css('script').extract()
            if 'https://www.google-analytics.com/analytics.js' in str(counters_anal):
                yee = 'Есть'
            else:
                yee = 'Нет'
            if 'mc.yandex.ru/metrika' in str(counters_anal):
                res = 'Есть'
            else:
                res = 'Нет'
            social = quote.css('a').extract(),
            if 'vk.com' or 'vk.me' in social:
                vk_stat = 'Есть'
            else:
                vk_stat = 'Нет'
            if 'facebook.com' in social:
                fb_stat = 'Eсть'
            else:
                fb_stat = 'Нет'
            if 'instagram.com' in social:
                insta_stat = 'Есть'
            else:
                insta_stat = 'Нет'
            urls = response.url

            title = quote.css('title::text').extract_first(),

            item['base_url'] = self.allowed_domains[0]
            item['title'] = Ch.check('title', title)
            description = quote.css(
                'meta[name*=description]::attr(content), meta[name*=Description]::attr(content)').extract(),
            h1 = quote.css('h1::text').extract(),
            h2 = quote.css('h2::text, H2::text').extract(),
            item['description'] = Ch.check('description', description)
            item['h1'] = Ch.check('h1', h1)
            item['h2'] = Ch.check('h2', h2)
            keyword = quote.css(
                'meta[name*=Keywords]::attr(content), meta[name*=keywords]::attr(content)').extract(),
            item['keyword'] = Ch.check('keywords', keyword)
            item['description_unique'] = description
            item['title_unique'] = title
            item['link'] = response.url
            item['broken_link'] = Li.check(response.status)
            item['img'] = len(quote.css('img').extract())
            item['alt'] = len(quote.css('img::attr(alt)').extract())
            text = quote.css('p::text, span::text').extract(),
            item['text'] = str(text),
            item['vk'] = vk_stat,
            item['facebook'] = fb_stat,
            item['instagram'] = insta_stat,
            item['googl_anal'] = yee,
            item['yandex_metrick'] = res,
            return item

    def get_url(self, url, short_url):
        self.start_urls.clear()
        self.allowed_domains.clear()
        self.url = url
        self.allowed_domains.append(short_url)
        self.start_urls.append(url)


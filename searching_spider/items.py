# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchingSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    base_url = scrapy.Field()
    title = scrapy.Field()
    keyword = scrapy.Field()
    description = scrapy.Field()
    title_unique = scrapy.Field()
    description_unique = scrapy.Field()
    broken_link = scrapy.Field()
    link = scrapy.Field()
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    vk = scrapy.Field()
    facebook = scrapy.Field()
    instagram = scrapy.Field()
    text = scrapy.Field()
    googl_anal = scrapy.Field()
    yandex_metrick = scrapy.Field()
    img = scrapy.Field()
    alt = scrapy.Field()
    html = scrapy.Field()


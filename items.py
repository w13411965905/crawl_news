# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy.item
class NewContext(scrapy.Item):
    title=scrapy.Field()
    text=scrapy.Field()
    author=scrapy.Field()
    type=scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field() 
    url=scrapy.Field()


'''
class CrawlNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author= scrapy.Field()
    type = scrapy.Field()
    text= scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
'''
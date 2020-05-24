# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    Url = scrapy.Field()
    Brand = scrapy.Field()
    Model = scrapy.Field()
    Memory_Type = scrapy.Field()
    Ram_Size = scrapy.Field()
    Price = scrapy.Field()

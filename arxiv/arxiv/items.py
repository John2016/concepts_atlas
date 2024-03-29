# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArxivItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title   =scrapy.Field()
    authors =scrapy.Field()
    comments=scrapy.Field()
    subjects=scrapy.Field()
    abstract=scrapy.Field()
    link    =scrapy.Field() 
    pass

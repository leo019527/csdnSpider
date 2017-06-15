# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    starttime = scrapy.Field()
    tag = scrapy.Field()
    title = scrapy.Field()
    istop = scrapy.Field()
    recommend = scrapy.Field()
    stoptime = scrapy.Field()
    content = scrapy.Field()
    usr = scrapy.Field()
    like = scrapy.Field()
    dislike = scrapy.Field()
    focus = scrapy.Field()
    collect = scrapy.Field()
    bankuai = scrapy.Field()
    pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdniosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field()
	href = scrapy.Field()


class TieziItem(scrapy.Item):
	startTime = scrapy.Field()
	tag = scrapy.Field()
	title = scrapy.Field()
	top = scrapy.Field()
	recommend = scrapy.Field()
	closeTime = scrapy.Field()
	content = scrapy.Field()
	user = scrapy.Field()
	like = scrapy.Field()
	dislike = scrapy.Field()
	guanzhu = scrapy.Field()
	shoucang = scrapy.Field()
	plate = scrapy.Field()

class yonghuItem(scrapy.Item):
	level = scrapy.Field()
	postNum = scrapy.Field()
	createTime = scrapy.Field()
	user = scrapy.Field()
	concerns = scrapy.Field()
	beConcerneds = scrapy.Field()
	updateTimes = scrapy.Field()

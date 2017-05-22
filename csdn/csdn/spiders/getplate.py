# -*- coding: utf-8 -*-
import scrapy


class GetplateSpider(scrapy.Spider):
    name = "getplate"
    start_urls = ['http://http://bbs.csdn.net/home/']

    def parse(self, response):
		sel = scrapy.Selector(response)

        pass

# -*- coding: utf-8 -*-
import scrapy


class GetpostSpider(scrapy.Spider):
	name = "getpost"
	start_urls = ['http://http://bbs.csdn.net/home/']

	def parse(self, response):
		sel = scrapy.Selector(response)
		url = sel.xpath('//div[@class="dropdown-menu"]').re('<a href="/forums/(.*)">')
		urlfront = "http://bbs.csdn.net/forums/"
		for i in range(0,len(url)-1):
			yield Request(urlfront+url[i],callback = self.parse2)
	
	def parse2(self,response):
		pass

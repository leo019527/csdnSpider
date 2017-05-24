# -*- coding: utf-8 -*-
import scrapy


class GetpostSpider(scrapy.Spider):
    name = "getpost"
    start_urls = ['http://http://bbs.csdn.net/home/']

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        url = sel.xpath('//div[@class="dropdown-menu"]').re('<a href="/forums/(.*)">')
        urlfront = "http://bbs.csdn.net/forums/"
        for i in range(0,len(url)-1):
            yield Request(urlfront+url[i],callback = self.parse2)
    
    def parse2(self,response):
        sel = scrapy.selector.Selector(response)
        href = sel.xpath('//table//tr//td[@class="title"]//a/@href').extract()
        hreffront = "http://bbs.csdn.net"
        for i in range(0,len(href)-1):
            yield Request(hreffront+href[i],callback = self.parse3)

    def parse3(self,response):
        sel = scrapy.selector.Selector(response)
        starttime = sel.xpath('//td[@class="post_info topic"]/div/span[@class="time"]/text()').re("[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*")[0]
        tag = sel.xpath('//div[@class="tag"]/span/a/text()').extract()
        title = sel.xpath('//span[@class="title text_overflow"]/text()').extract()[0]
        
        pass

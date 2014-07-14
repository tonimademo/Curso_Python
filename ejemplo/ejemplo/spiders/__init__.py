# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from myproject.items import MyItem

class Rastreador(BaseSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
    'http://osl.ugr.es/'
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for h3 in hxs.select('//h3').extract():
            yield MyItem(title=h3)
            for url in hxs.select('//a/@href').extract():
                yield Request(url, callback=self.parse)

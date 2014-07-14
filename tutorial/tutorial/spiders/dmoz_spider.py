from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import Contenedor


def imprimir(string):
	"""Return complete url"""
	return "http://osl.ugr.es/" + string

class DmozSpider(BaseSpider):

	name = "dmoz"
	allowed_domains = ["osl.ugr.es"]
	start_urls = [
		"http://osl.ugr.es/"
	]
	
	def parse(self, response):
		items = []
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//div[@class = "entry hentry"]')
		
		for site in sites:
			elemento= Contenedor()
			elemento['title']= sites.select('//a[@title]/text()').extract()
			elemento['author']= sites.select('//a[@class = "url fn"]/text()').extract()
			elemento['cont']= sites.select('//div[@class]/p/text()').extract()
			items.append(elemento)
			print "uno"
		return items
			
'''
	name = 'dmoz'
	start_urls = [
		'http://www.bhinneka.com/categories.aspx'
	]
	def complete_url(string):
		"""Return complete url"""
		return "http://www.bhinneka.com" + string
 
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		# HXS to find url that goes to detail page
		items = hxs.select('//div[@id="ctl00_content_divContent"]//li[@class="item"]/a[2]/@href')
		for item in items:
			link = item.extract()
			print complete_url(link)
'''

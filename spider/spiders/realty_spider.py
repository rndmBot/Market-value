# -*- coding: utf-8 -*-
import scrapy


class RealtySpiderSpider(scrapy.Spider):
	name = 'realty_spider'
	start_urls = [f'https://dom.ria.com/nedvizhimost/?page={i}' for i in range(1, 13011)]

	def parse(self, response):
		for section in response.css('#catalogResults section.ticket-clear'):

			item = {}
			item['parse'] = section.css('a.blue::attr(href)').extract_first()

			parse2 = section.css('a.blue::text, a.blue > span::text').extract()
			if parse2:
				item['parse2'] = ' '.join([line.replace('\xa0', ' ').replace(',', '').strip() for line in parse2]).strip().replace('\xb2', ' кв').replace('\u2011', '-')        	 
			else:
				item['parse2'] = ''

			item['price_usd'] = section.css('div.mb-5 span b.green::text').extract_first()
			item['parse3'] = ' '.join(section.css('ul.mb-10 li:not(.hide)::text').extract()).replace('\xb2', ' кв')

			yield item
# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'centris'
    allowed_domains = ['www.centris.ca']

    script = '''
        function main(splash, args)
            splash.private_mode_enabled = False
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            rur_tab = assert(splash:select_all(".shell"))
            assert(splash:wait(1))
            splash:set_viewport_full()
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url='https://www.centris.ca/en/commercial-properties~for-sale?view=Thumbnail&uc=0', callback=self.parse, endpoint='execute', args={
            'lua_source': self.script
        })

    def parse(self, response):
        quotes = response.xpath("//div[@class='shell']")
        for quote in quotes:
            yield {
                'price': quote.xpath(".//div[@class='price']/span[1]/text()").get(),
                'category': quote.xpath("normalize-space(.//span[@class='category']/div/text())").get()
                # 'address': quote.xpath(".//span[@class='address']/div/text()").get()
            }
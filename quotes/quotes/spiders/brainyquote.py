import scrapy


class BrainyquoteSpider(scrapy.Spider):
    name = 'brainyquote'
    allowed_domains = ['www.brainyquote.com']
    start_urls = ['https://www.brainyquote.com/topics/daily-quotes']

    def parse(self, response):
        box = response.xpath("//div[@class = 'grid-item qb clearfix bqQt']")
        for txt in box:
            yield{
            'quote':  txt.xpath("normalize-space(.//div[@style = 'display: flex;justify-content: space-between']/text())").extract(),
            'author' : txt.xpath(".//a[@title='view author']/text()").extract()
            }


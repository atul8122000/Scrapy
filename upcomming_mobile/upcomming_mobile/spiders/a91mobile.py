import scrapy


class A91mobileSpider(scrapy.Spider):
    name = '91mobile'
    allowed_domains = ['www.91mobiles.com']
    start_urls = ['https://www.91mobiles.com/upcoming-mobiles-in-india']

    def parse(self, response):
        index = response.xpath("//div[@class= 'filter filer_finder']")

        for item in index:
            yield{
                'name': item.xpath(".//a[@class= 'hover_blue_link name gaclick']/text()").extract(),
                'Price':item.xpath(".//span[@class= 'price price_float']/text()").extract(),
                'launch_date':item.xpath(".//div[@class= 'pro_list_date']/text()").extract()
            }
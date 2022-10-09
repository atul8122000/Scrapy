# import scrapy

# class ExampleSpider(scrapy.Spider):
#     name = 'del'
 
#     product ='defense'

#     def start_requests(self):
#         # for product in self.products:
#             yield scrapy.Request(
#                 url = f'https://www.justice.gov/news?keys={self.product}&items_per_page=25',
#                 callback = self.parse
#             )
#     def parse(self,response):
#         links = response.xpath("//span[@class='field-content']/a")
#         for link in links:
#             link = link.xpath(".//@href").get()
#             yield response.follow(url=link, callback=self.parse_justice)


#     def parse_justice(self, response):
#         name = response.xpath("(//h1)[2]/text()").get()
#         date = response.xpath("//span[@class='date-display-single']/text()").get()
#         topic = response.xpath("(//div[@class='field__items']/div[@class='field__item even'])[3]/text()").get()
#         component = response.xpath("(//div[@class='field__items']/div[@class='field__item even'])[4]/text()").get()
#         press_release = response.xpath("(//div[@class='field__items']/div[@class='field__item even'])[5]/text()").get()

#         yield {
#             '_id' : name,
#             'date': date,
#             'topic': topic,
#             'component': component,
#             'press_release': press_release
#             }

#         next_page = response.xpath("//li[@class='pager__item pager__item--next']/a/@href").get()
#         if next_page:
#             abs_url = f"https://www.justice.gov{next_page}"
#         yield scrapy.Request(
#             url=abs_url,
#             callback=self.parse_justice
#         )
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'del'
    allowed_domains = ['www.justice.gov']
    start_urls = ['https://www.justice.gov/news?keys=security&items_per_page=25']

    def parse(self,response):
        links = response.xpath("//span[@class='field-content']/a")
        for link in links:
            link = link.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_justice)


    def parse_justice(self, response):
        name = response.xpath("(//h1)[2]/text()").get()
        date = response.xpath("//span[@class='date-display-single']/text()").get()
        topic = response.xpath("(//div[@class='field__items']/div[@class='field__item even'])[3]/text()").get()
        component = response.xpath("(//div[@class='field__items']/div[@class='field__item even'])[4]/text()").get()
        press_release = response.xpath("(//div[@class='field__items']/div[@class='field__item even'])[5]/text()").get()

        yield {
            '_id' : name,
            'date': date,
            'topic': topic,
            'component': component,
            'press_release': press_release
            }
        next_page = response.xpath("//li[@class='pager__item pager__item--next']/a/@href").get()
        if next_page:
            yield scrapy.Request(url=f"https://www.justice.gov{next_page}", callback=self.parse)

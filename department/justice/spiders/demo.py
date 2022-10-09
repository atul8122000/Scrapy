import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'demo'
 
    # product = input("Enter keyword for search: ")
    
    # def start_requests(self):
    #     yield scrapy.Request(
    #         url = f'https://www.justice.gov/news?keys={self.product}&items_per_page=25',
    #         callback = self.parse
    #     )
    products = ['defense', 'complaint', 'security']
    
    def start_requests(self):
        for product in self.products:
            yield scrapy.Request(
                url = f'https://www.justice.gov/news?keys={product}&items_per_page=25',
                callback = self.parse
            )

    def parse(self,response):
        links = response.xpath("//span[@class='field-content']/a")
        for link in links:
            link = link.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_justice)


    def parse_justice(self, response):

        topic = response.xpath("(//div[@class='pr-fields']//div[@class='field__items']/div[@class='field__item even'])[1]/text()").get()
        component = response.xpath("//div[@class='field__items']/div[@class='field__item even']/a/text()").get()
    

        
        

        yield {
         
            'topic': topic,
            'component': component
  
            }
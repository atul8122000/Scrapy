import scrapy
from ..items import ImageItem

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['www.shutterstock.com']
    start_urls = ['https://www.shutterstock.com/category/education']

    def parse(self, response):
        image = ImageItem()        
        img_urls = []
        for img in response.xpath("//div[@class='z_h_b900b']//img[@class='z_h_6a355 z_h_9d80b z_h_2f2f0']/@src").extract():
            img_urls.append(img)

        image["image_urls"] = img_urls

        return image
import scrapy
from ..items import ImageItem

class ImgSpider(scrapy.spiders.Spider):
    name = 'example'
    allowed_domains = ['www.imagesbazaar.com']
    start_urls = ['https://www.imagesbazaar.com/advancesearchresult/computer/computer/0/0/0/0/0/0/0/0/0']

    def parse(self, response):
        image = ImageItem()        
        img_urls = []
        for img in response.xpath("//div[@class=' card productItemLarge280 H']/img/@src").extract():
            img_urls.append(img)

        image["image_urls"] = img_urls

        return image
            

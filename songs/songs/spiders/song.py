import scrapy
from ..items import SongsItem


class ImgSpider(scrapy.spiders.Spider):
    name = 'song'
    allowed_domains = ['www.pagalworld.pw']
    start_urls = ['https://www.pagalworld.pwz']

    def parse(self, response):
        url = response.xpath("//li[@class='tnned']/div[2]/h3/a/@hraf")
        for song in url:
            
            link = song.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_country)


    def parse_country(self, response):
        Song = SongsItem()
        song_urls = []
        
        s = response.xpath(".//div[@class='downloaddiv'][2]/a@href").get()
        song_urls.append(s)
        Song["song_urls"] = song_urls

        return Song

            
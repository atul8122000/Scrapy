import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.bollywoodhungama.com']
    start_urls = ['https://www.bollywoodhungama.com/movie-release-dates/']

    def parse(self, response):
        row = response.xpath("//tbody/tr")
        for detail in row:
            yield{
                'release_date': detail.xpath(".//td[1]/text()").get(),
                'Movie_name': detail.xpath(".//td[2]/a/text()").get(),
                'audience_score': detail.xpath(".//td[@class='TAR']/span/text()").get()
            }
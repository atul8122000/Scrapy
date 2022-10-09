import scrapy


class GdpSpider(scrapy.Spider):
    name = 'asian_countries_gdp'
    allowed_domains = ['www.populationu.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-gdp']

    def parse(self, response):
        countries = response.xpath("(//table[@class='jsx-1878461898 table table-striped tp-table-body'])[4]/tbody/tr")
        
        for country in countries:
            rank = country.xpath(".//td[1]/text()").get()
            name = country.xpath(".//td/a/text()").get()
            GDP_Per_Capita = country.xpath(".//td[5]/text()").get()
            Population = country.xpath(".//td[6]/text()").get()
            yield{
                'rank': rank,
                'Name': name,
                'GDP_Per_Capita' : GDP_Per_Capita,
                'Population': Population
                
                }

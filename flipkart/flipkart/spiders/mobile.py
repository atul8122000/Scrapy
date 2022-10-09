import scrapy


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/mobiles/pr?sid=tyy,4io&p[]=facets.brand%255B%255D%3DPOCO&otracker=clp_metro_expandable_2_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_O1WYX08RHODP_wp3&fm=neo%2Fmerchandising&iid=M_2549515f-2b9a-41e1-bdca-7769c51836d6_3.O1WYX08RHODP&ppt=hp&ppn=homepage&ssid=zsjhesoods0000001647838321882']

    def parse(self, response):
        mobiles =response.xpath("//div[@class= '_2kHMtA']") 
        for mobile in mobiles:
            yield{
                'Name':mobile.xpath(".//div[@class= '_4rR01T']/text()").get(),
                'Disconted Price':mobile.xpath(".//div[@class= '_30jeq3 _1_WHN1']/text()").get(),
                'original Price':mobile.xpath(".//div[@class= '_3I9_wc _27UcVY']/text()[2]").get(),
                'discount':mobile.xpath(".//div[@class= '_3Ay6Sb']/span/text()").get()
            }

        next_page = response.urljoin(response.xpath("//nav[@class= 'yFHi8N']/a[@class= 'ge-49M']/@href").get())
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse ,dont_filter=True)
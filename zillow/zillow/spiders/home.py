import scrapy


class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['www.zillow.com']
    start_urls = ['https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.921332%2C%22east%22%3A-69.780707%2C%22south%22%3A23.10845930709574%2C%22north%22%3A51.0333985198548%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%7D']
    
    
    def parse(self,response):
        links = response.xpath("//div[@class='StyledPropertyCardPhotoBody-c11n-8-69-2__sc-128t811-0 clrcsE']")
        for link in links:
            link = link.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_home)


    def parse_home(self, response):
        price = response.xpath("//span[@class='Text-c11n-8-65-2__sc-aiai24-0 dpf__sc-1me8eh6-0 cWepYI fzJCbY']//text()").get(),
        bds = response.xpath("(//span[@class='Text-c11n-8-65-2__sc-aiai24-0 kpJbvM']/strong)[1]/text()").get(),
        ba = response.xpath("(//span[@class='Text-c11n-8-65-2__sc-aiai24-0 kpJbvM']/strong)[2]/text()").get(),
        Add = response.xpath("(//h1[@class='Text-c11n-8-65-2__sc-aiai24-0 kpJbvM'])[1]/text()").get(),
        Type = response.xpath("(//span[@class='Text-c11n-8-65-2__sc-aiai24-0 dpf__sc-2arhs5-3 kpJbvM btxEYg'])[1]/text()").get(),

        yield {
            'price' : price,
            'bds':bds,
            'ba': ba,
            'Add': Add,
            'Type': Type
        }


    # def parse(self, response):
    #     homes =response.xpath("//div[@class='StyledCard-c11n-8-69-2__sc-rmiu6p-0 hYanUy StyledPropertyCardBody-c11n-8-69-2__sc-1p5uux3-0 bDmKKM']")
    #     for home in homes:
    #         yield{
    #             'price': home.xpath(".//div[@class='StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 kJFQQX']/span/text()").get()
                # 'bds': home.xpath(".(//span[@class='StyledPropertyCardHomeDetails-c11n-8-69-2__sc-1mlc4v9-0 ereqYj']/span/text())[2]").get(),
                # 'ba': home.xpath(".(//span[@class='StyledPropertyCardHomeDetails-c11n-8-69-2__sc-1mlc4v9-0 ereqYj']/span/text())[4]").get(),
                # 'sqft': home.xpath(".(//span[@class='StyledPropertyCardHomeDetails-c11n-8-69-2__sc-1mlc4v9-0 ereqYj']/span/text())[6]").get(),
                # 'Add': home.xpath("//address[@data-test='property-card-addr']/text()").get()
            # }

        # next_page = response.urljoin(response.xpath("//li[@class='PaginationJumpItem-c11n-8-69-2__sc-18wdg2l-0 kAlpJR'][2]/@href").get())
        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse ,dont_filter=True)

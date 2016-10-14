import scrapy

class YellowPageScraper(scrapy.Spider):
    name = 'yellow_page_scraper'

    def start_requests(self):
        urls = [
            'http://www.bangladeshyellowpages.com/category'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # Baseurl
        baseurl = 'http://www.bangladeshyellowpages.com/category'

        # Getting the names of the available categories
        categories = response.xpath("//div[@class='listing']/ul/li//a[@href]/text()").extract()

        # Gets the number of item per category
        items = numberofitems = [int(item.lstrip().rstrip().replace(' items', '')) for item in response.xpath("//div[@class='listing']/ul/li/text()[2]").extract()]

        categories_url = [baseurl + url for url in response.xpath("//div[@class='listing']/ul/li//@href").extract()]

        print "Categories: ", categories , categories_url

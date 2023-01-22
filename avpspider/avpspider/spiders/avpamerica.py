import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'avpamerica'
    start_urls = ['https://avpamerica.com/VA-Beach-Volleyball-Player-Rankings.aspx']

    def parse(self, response):
        filename = f'avpamerica.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
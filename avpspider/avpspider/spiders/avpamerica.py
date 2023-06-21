import scrapy
import os

class AVPamericaSpider(scrapy.Spider):

    # Name of the spider
    name = 'avpamerica'

    # The domain to be scraped
    allowed_domains = ['avpamerica.com']

    # The URLs to be scraped from the domain
    start_urls = ['https://avpamerica.com/VA-Beach-Volleyball-Player-Rankings.aspx']

    # Default callback method
    def parse(self, response):

        filedir = os.getcwd()
        filename = f'avpamerica.html'

        with open(filename, 'wb') as f:
            f.write(response.body)

        self.logger.info(f'Saved file {filedir}/{filename}')
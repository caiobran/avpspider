import os
import scrapy
from scrapy.selector import Selector


class AVPamericaSpider(scrapy.Spider):

    # Name of the spider
    name = 'avpamerica'

    # The domain to be scraped
    allowed_domains = [
        'avpamerica.com'
    ]

    # The URLs to be scraped from the domain
    start_urls = [
        'https://avpamerica.com/VA-Beach-Volleyball-Player-Rankings.aspx'
    ]

    # Default callback method
    def parse(self, response):

        sel = Selector(text=response.body)

        a_tags = sel.xpath('//a')

        # Parse player ranking table
        #rank = sel.xpath('//*[@id="Table2"]/tbody/tr/td[1]')
        #name = sel.xpath('//*[@id="Table2"]/tbody/tr/td[2]')
        #hometown = sel.xpath('//*[@id="Table2"]/tbody/tr/td[3]')
        #points = sel.xpath('//*[@id="Table2"]/tbody/tr/td[4]')
        
        # Save html reponse to file
        #filedir = os.getcwd()
        #filename = f'avpamerica.html'
        #filepath = os.path.join(filedir, filename)
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.logger.info(f'Saved file {filepath}')
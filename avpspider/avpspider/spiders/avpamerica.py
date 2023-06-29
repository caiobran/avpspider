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

        yield {
            'date': response.headers['Date'],
            'title': response.xpath('//html/head/title/text()').get().strip(),
            'url': response.url,
            'status': response.status,
            'headers': response.headers,
            'enconding': response.encoding,
            'text': response.text
        }

        # Get rows of player rank table
        query = '//*[@id="Table2"]/tbody/tr[not(./th) and not(./td[@colspan])]'
        tbl_rows = response.xpath(query).getall()

        # Get player profile links
        query = '//*[@id="Table2"]/tbody/tr/td[1][not(@colspan)]'
        player_ranks = response.xpath(query).getall()

        query = '//*[@id="Table2"]/tbody/tr/td[2]'
        player_names = response.xpath(query).getall()

        query = '//*[@id="Table2"]/tbody/tr/td[2]/span/a/@href'
        player_links = response.xpath(query).getall()

        query = '//*[@id="Table2"]/tbody/tr/td[3]'
        player_hometowns = response.xpath(query).getall()

        query = '//*[@id="Table2"]/tbody/tr/td[4]'
        player_points = response.xpath(query).getall()
        

        self.logger.info(f'Parsed URL: {response.url}')
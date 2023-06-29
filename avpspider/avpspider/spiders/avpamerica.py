import os
import re
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

        page_title = response.xpath('//html/head/title/text()').get().strip()

        self.logger.info(f'Parsing "{page_title}" | URL: {response.url}')

        yield {
            'date': response.headers['Date']
            ,'title': page_title
            ,'url': response.url
            # ,'status': response.status
            # ,'headers': response.headers
            # ,'enconding': response.encoding
            # ,'text': response.text
        }

        if 'VA-Beach-Volleyball-Player-Rankings.aspx' in response.url:
                
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
            
            yield from response.follow_all(player_links[0:4], callback=self.parse)

        elif 'VA-Volleyball-Player-Stats.aspx' in response.url:

            pattern = 'ID=(\d+)'
            player_id = re.findall(pattern, response.url)[0]
            
            pattern = 'LeagueID=(-{0,1}\d+)'
            player_league_id = re.findall(pattern, response.url)[0]


        self.logger.info(f'Parsed "{page_title}" | URL: {response.url}')

        # yield from response.follow_all(all_links, callback=self.parse)
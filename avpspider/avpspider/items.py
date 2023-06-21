# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AvpLink:
    # define the fields for your item here like:
    url:    Optional[str] = field(default=None)
    body:   Optional[str] = field(default=None)
    header: Optional[str] = field(default=None)
    status: Optional[int] = field(default=None)
    

@dataclass
class AvpPlayerRank:
    # define the fields for your item here like:
    name:     Optional[str] = field(default=None)
    hometown: Optional[str] = field(default=None)
    rank:     Optional[int] = field(default=None)
    points:   Optional[int] = field(default=None)
    

#class AvpspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    #pass

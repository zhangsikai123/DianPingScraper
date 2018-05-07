import scrapy

# Created by Sikai on 2018/04/19.

class Seed(scrapy.Item):
    _id = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    code = scrapy.Field()
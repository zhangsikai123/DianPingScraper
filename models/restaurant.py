import scrapy

# Created by Sikai on 2018/04/19.

class Restaurant(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    tel = scrapy.Field()
    address = scrapy.Field()
    open_time = scrapy.Field()
    cata1 = scrapy.Field()
    cata2 = scrapy.Field()
    area = scrapy.Field()
    comment = scrapy.Field()
    avg_money_spent = scrapy.Field()
    star = scrapy.Field()
    tag1 = scrapy.Field()
    tag2 = scrapy.Field()
    tag3 = scrapy.Field()
    all_tags = scrapy.Field()
import scrapy

class Url(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    province = scrapy.Field()
    address = scrapy.Field()
    review_num = scrapy.Field()
    mean_price = scrapy.Field()
    star_num = scrapy.Field()
    taste = scrapy.Field()
    environment = scrapy.Field()
    service = scrapy.Field()
    dish_tag = scrapy.Field()
    addr_tag = scrapy.Field()
    pic_url = scrapy.Field()
    recommends = scrapy.Field()

# -*- coding: UTF-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# Created by Sikai on 2018/04/19.
import pymongo
from bs4 import BeautifulSoup
from scrapy.conf import settings
from scrapy.exceptions import DropItem

from models import crawling_seed


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(host = settings['MONGODB_HOST'], port = settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DBNAME']]
        self.url_collection = db['urls_new']
        self.restaurant_collection = db['restaurants']

    def update(self, collection, item):
        try:
            collection.insert(dict(item))
            return item
        except:
            raise DropItem('Item already exists.')

    def process_item(self, item, spider):
        if spider.name == 'urlSpider':
            self.update(self.url_collection, item)
        if spider.name == 'restaurantSpider':
            self.update(self.restaurant_collection, item)

class DazhongdianpingPipeline(object):
    def process_item(self, item, spider):
        return item



def main():
    # connection = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
    # db = connection[settings['MONGODB_DBNAME']]
    # collection = db['crawling_seeds']
    #
    # prefix = '/Users/zhangsikai/Desktop/dianpingPages/'
    # suffix ='.htm'
    # htmls = []
    # for i in range(1,17):
    #     html = open(prefix + str(i) + suffix).read()
    #     htmls.append([i,html])
    # for id, html in htmls:
    #     soup = BeautifulSoup(html, 'lxml', from_encoding = 'utf-8')
    #     alist = soup.find('div','nav-category nav-tabs J_filter_region').find("div","nc-items nc-sub nc-more ")
    #     if alist == None:
    #         alist = soup.find('div','nav-category nav-tabs J_filter_region').find("div","nc-items nc-sub ") #也许没有更多
    #     alist = alist.find_all('a')
    #     for a in alist:
    #         url = a['href']
    #         seed = crawling_seed.Seed()
    #         if url.startswith('java'):
    #             continue
    #         seed['_id'] = 'location' + url
    #         seed['tag'] = 'location'
    #         seed['url'] = url
    #         seed['name'] = a.get_text()
    #         seed['code'] = url[37:]
    #         try:
    #             collection.insert(seed)
    #         except:
    #             continue
    import wrappers.url_wrapper as wrapper
    with open('/Users/zhangsikai/Desktop/dianpingPages/1.htm','r') as f:
        html = f.read()
        items = wrapper.wrap(html)
        for item in items:
            print item
if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-

# Created by Saki on 2016/12/21.

import urlparse
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.conf import settings
from models import url

class urlSpider(CrawlSpider):
    name = 'urlSpider'
    redis_key = 'urlSpider:start_urls'
    prefix = 'http://www.dianping.com/beijing/ch10/'

    start_urls = [prefix + category + district for category in settings['CATEGORY'] for district in settings['DISTRICT']]

    url = 'http://www.dianping.com/search/category/2/10'

    def parse(self, response):
        html = response.body
        soup = BeautifulSoup(html, 'lxml', from_encoding = 'utf-8')
        shop_list = soup.find('div', class_ = 'shop-list J_shop-list shop-all-list')
        lis = shop_list.find_all('li')
        for li in lis:
            tit = li.find('div', class_ = 'tit')
            name = tit.a.h4.get_text()
            page = tit.a['href']
            item = url.Url()
            item['_id'] = page.replace('/shop/', '')
            item['name'] = name
            item['url'] = urlparse.urljoin(self.url, page)
            yield item
        next_page = soup.find('a', class_ = 'next')
        if next_page is not None:
            next_url = urlparse.urljoin(self.url, next_page['href'])
            yield Request(next_url, callback = self.parse)


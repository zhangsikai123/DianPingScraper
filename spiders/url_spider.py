# -*- coding: utf-8 -*-

# Created by Sikai on 2018/04/19.

import urlparse
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.conf import settings
from wrappers import url_wrapper
class urlSpider(CrawlSpider):

    name = 'urlSpider'

    redis_key = 'urlSpider:start_urls'

    start_urls = settings['START_URLS']

    url = 'http://www.dianping.com/search/category/2/10'

    cnt = 0

    def parse(self, response):
        html = response.body
        soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
        try:
            items = url_wrapper.wrap(html)
        except:
            items = []
        for item in items:
            yield item
        next_page = soup.find('a', class_ = 'next')

        if next_page is not None:
            next_url = urlparse.urljoin(self.url, next_page['href'])
            yield Request(next_url, callback = self.parse)
            
# -*- coding: utf-8 -*-

# Created by Sikai on 2018/04/19.

from scrapy import cmdline

# cmdline.execute('scrapy crawl urlSpider'.split())
# cmdline.execute('scrapy crawl shopSpider'.split())
# cmdline.execute('scrapy crawl commentSpider'.split())
cmdline.execute('scrapy crawl urlSpider -s DOWNLOAD_DELAY=1'.split())
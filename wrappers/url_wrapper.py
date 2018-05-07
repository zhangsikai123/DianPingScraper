import urlparse
from bs4 import BeautifulSoup
from models import url
# Created by Sikai on 2018/04/19.

#wrapper for URL model
def wrap(page):
    soup = BeautifulSoup(page, 'lxml', from_encoding='utf-8')
    shop_list = soup.find('div', class_='shop-list J_shop-list shop-all-list')
    lis = shop_list.find_all('li')
    items = []
    for li in lis[:1]:
        items.append(wrap_item(li))
    return items



def _get_star(comment):
    try:
        return comment.find_all('span')[0]['class'][1][-2]
    except:
        return ''

def _get_review_num(comment):
    try:
        return comment.find('a', class_='review-num').find_all('b')[0].get_text()
    except:
        return ''

def _get_mean_price(comment):
    try:
        return comment.find('a', class_='mean-price').find_all('b')[0].get_text()[1:]
    except:
        return ''

def _get_tags(li):
    tags = []
    spans = li.find('span', class_='comment-list')
    if spans is None:
        return ['','','']
    for tag in spans.find_all('span'):
        if tag is None or len(tag.find_all('b'))<1:
            tags.append('')
        else:
            tags.append(tag.find_all('b')[0].get_text())
    return tags

def _get_pic(li):
    try:
        return li.find('div', class_='pic').a.img['data-src']
    except:
        return ''

def _get_recommended_dish(li):
    res = {}
    try:
        alist = li.find('div','txt').find('div','recommend').find_all('a')
    except:
        return res
    for a in alist:
        try:
            res[a.get_text()] = a['href']
        except:
            res[a.get_text()] = ''
    return res

def _get_address(tag_addr):
    try:
        return tag_addr.find('span', class_='addr').get_text()
    except:
        return ''

def _get_addr_tag(tag_addr):
    try:
        return tag_addr.find('span','tag').get_text()
    except:
        return ''

def _get_dish_tag(tag_addr):
    try:
        return tag_addr.find('span','addr').get_text()
    except:
        return ''

def wrap_item(li):
    default = "http://www.dianping.com/search/category/2/10"
    comment = li.find('div', class_='comment')
    tit = li.find('div', class_='tit')
    tag_addr = li.find('div', class_='tag-addr')

    name = tit.a.h4.get_text()
    page = tit.a['href']

    tags = _get_tags(li)

    star_num = _get_star(comment)
    review_num = _get_review_num(comment)
    mean_price = _get_mean_price(comment)

    dish_tag = _get_dish_tag(tag_addr)
    addr_tag = _get_addr_tag(tag_addr)
    address = _get_address(tag_addr)
    pic_url = _get_pic(li)
    recommends = _get_recommended_dish(li)

    item = url.Url()
    item['_id'] = page.replace('/shop/', '')
    item['name'] = name
    item['url'] = urlparse.urljoin(default, page)
    item['province'] = 'Beijing'
    item['address'] = address
    item['review_num'] = review_num
    item['star_num'] = star_num
    item['mean_price'] = mean_price
    item['taste'] = tags[0]
    item['environment'] = tags[1]
    item['service'] = tags[2]
    item['dish_tag'] = dish_tag
    item['addr_tag'] = addr_tag
    item['pic_url'] = pic_url
    item['recommends'] = recommends
    return item
import urllib3

def main():
    url = 'http://www.dianping.com/shop/37770315'
    url = 'http://www.baidu.com'
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": "http-dyn.abuyun.com",
        "port": "9020",
        "user": 'H5LY20427XLM641D',
        "pass": 'C8CE061D635B6E3D',
    }
    print proxyMeta
    proxy = urllib3.ProxyManager(proxyMeta)
    http = urllib3.PoolManager()
    page = proxy.request('GET',url)
    print page.data
if __name__ == '__main__':
    main()
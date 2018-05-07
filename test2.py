import urllib2

def main():
    targetUrl = "http://www.dianping.com"

    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"


    proxyUser = "H5LY20427XLM641D"
    proxyPass = "C8CE061D635B6E3D"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxy_handler = urllib2.ProxyHandler({
        "http"  : proxyMeta,
        "https" : proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()

    print resp

if __name__ == '__main__':
    main()
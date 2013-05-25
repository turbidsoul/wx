# -*- coding: utf8 -*-

email = 'xxxxxxxxxxxxxxxxxx@email.com'
password = 'xxxxxxxxxxxxxxx'
header = [(
    'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    ('Accept-Charset', 'GBK,utf-8;q=0.7,*;q=0.3'),
    ('Accept-Encoding', 'gzip,deflate,sdch'),
    ('Cache-Control', 'max-age=0'),
    ('Connection', 'keep-alive'),
    ('Host', 'mp.weixin.qq.com'),
    ('Origin', 'mp.weixin.qq.com'),
    ('X-Requested-With', 'XMLHttpRequest'),
    ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 '
     '(KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22')]

# wx url
login_url = "http://mp.weixin.qq.com/cgi-bin/login?lang=en_US"
send_msg_referer_url = 'http://mp.weixin.qq.com/cgi-bin/singlemsgpage?fromfakeid=%s&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN'
single_send_url = 'https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN'
contact_url = 'https://mp.weixin.qq.com/cgi-bin/getcontactinfo?t=ajax-getcontactinfo&lang=zh_CN&fakeid=%s'

# weather url
weather1_url = "http://www.weather.com.cn/data/sk/%d.html"
weather2_url = "http://www.weather.com.cn/data/cityinfo/%d.html"
weather3_url = "http://m.weather.com.cn/data/%d.html"

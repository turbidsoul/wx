# -*- coding: utf8 -*-


# wx config
token = "wxturbidsoul"
wx_email = 'td816@163.com'
wx_password = 'ubuntulinux'
wx_header = [(
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

wx_login_url = "http://mp.weixin.qq.com/cgi-bin/login?lang=en_US"
wx_send_msg_referer_url = 'http://mp.weixin.qq.com/cgi-bin/singlemsgpage?fromfakeid=%s&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN'
wx_single_send_url = 'https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN'
wx_contact_info_url = 'https://mp.weixin.qq.com/cgi-bin/getcontactinfo?t=ajax-getcontactinfo&lang=zh_CN&fakeid=%s'
wx_contact_url = 'https://mp.weixin.qq.com/cgi-bin/contactmanagepage?token=%s&t=wxm-friend&lang=zh_CN&pagesize=10&pageidx=0&type=0&groupid=%d'
wx_index_url = 'https://mp.weixin.qq.com/cgi-bin/indexpage?t=wxm-index&token=%s&lang=zh_CN'

wx_ungrouped = 0
wx_blacklist = 1
wx_starred = 2

# weather url
weather_base_url = 'www.weather.com.cn'
weather1_url = "http://www.weather.com.cn/data/sk/%s.html"
weather2_url = "http://www.weather.com.cn/data/cityinfo/%s.html"
weather3_url = "http://m.weather.com.cn/data/%s.html"

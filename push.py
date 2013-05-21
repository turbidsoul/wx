# -*- coding: utf8 -*-

import hashlib
import urllib
import urllib2
import json
import poster
import cookielib
import time


class Push(object):

    """
    推送消息
    """

    login_url = "http://mp.weixin.qq.com/cgi-bin/login?lang=en_US"
    referer_url = 'http://mp.weixin.qq.com/cgi-bin/singlemsgpage?fromfakeid=%s&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN'
    single_send_url = 'https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN'

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    def login(self):
        pass


class ClientLoginException(Exception):
    pass


email = "td816@163.com"
password = "ubuntulinux"

login_url = "http://mp.weixin.qq.com/cgi-bin/login?lang=en_US"

m = hashlib.md5(password[:])
m.digest()
pw = m.hexdigest()

body = (
    ('username', email),
    ('pwd', pw),
    ('imgcode', ''),
    ('f', 'json')
)


opener = poster.streaminghttp.register_openers()
opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
opener.addheaders = [(
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

try:
    msg = json.loads(opener.open(
        login_url, urllib.urlencode(body), timeout=5).read())
except Exception as e:
    raise ClientLoginException
if msg['ErrCode'] not in (0, 65202):
    raise ClientLoginException
token = msg['ErrMsg'].split('=')[-1]
time.sleep(1)


print(token)

sendTo = "5636455"
data = {
    'type': 1,
    'content': '测试推送'
}

opener.addheaders += [('Referer', 'http://mp.weixin.qq.com/cgi-bin/singlemsgpage?fromfakeid={0}'
                      '&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN'.format(sendTo))]
body = {
    'error': 'false',
    'token': token,
    'tofakeid': sendTo,
    'ajax': 1}
body.update(data)
try:
    msg = json.loads(opener.open("https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&"
                                 "lang=zh_CN", urllib.urlencode(body), timeout=5).read())['msg']
except urllib2.URLError as e:
    time.sleep(1)
    print(e)

print(msg)

# -*- coding: utf8 -*-

import hashlib
import urllib
import urllib2
import json
import poster
import cookielib
import time
import settings
import logging


class Push(object):

    """
    推送消息
    """

    login_url = "http://mp.weixin.qq.com/cgi-bin/login?lang=en_US"
    referer_url = 'http://mp.weixin.qq.com/cgi-bin/singlemsgpage?fromfakeid=%s&msgid=&source=&count=20&t=wxm-singlechat&lang=zh_CN'
    single_send_url = 'https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN'
    push_msg_type = {
        'text': 1,
        'img': 2,
        'img_and_text': 10,
        'audio': -1,
        'video': -1,
    }

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = None
        if password:
            self.password = hashlib.md5(password).hexdigest()

    def login(self):
        if not self.email:
            self.email = settings.email
        if not self.password:
            self.password = hashlib.md5(settings.password).hexdigest()
        self.email = settings.email
        self.body = self.gen_body('login')

        self.opener = poster.streaminghttp.register_openers()
        self.opener.add_handler(
            urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
        self.opener.addheaders = settings.header
        try:
            msg = json.loads(self.opener.open(
                self.login_url, urllib.urlencode(self.body), timeout=5).read())
        except Exception as e:
            raise PushException(e)
        if msg['ErrCode'] not in (0, 65202):
            raise PushException(msg)
        self.token = msg['ErrMsg'].split('=')[-1]
        time.sleep(1)

    def gen_body(self, type, fake_id=None):
        body = {}
        if body == 'login':
            body['username'] = self.email
            body['pwd'] = self.password
            body['imgcode'] = ''
            body['f'] = 'json'
        elif body == 'push':
            body['error'] = 'false'
            body['token'] = self.token
            body['tofakeid'] = fake_id
            body['ajax'] = 1
        return body

    def send_txt_msg(self, send_to, msg):
        data = {
            'type': self.push_msg_type['text'],
            'content': msg
        }

        self.opener.addheaders['Referer'] = self.referer_url % str(send_to)
        body = self.gen_body('push', send_to)
        body.update(data)
        try:
            msg = json.loads(self.opener(self.single_send_url, urllib.urlencode(body), timeout=5).read())
        except urllib2.URLError, e:
            logging.error(e.message, e)
            return False

        if msg['msg'] == 'ok':
            return True


class PushException(Exception):
    pass

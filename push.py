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
from util import singleton


@singleton
class Push(object):

    """
    推送消息
    """
    push_msg_type = {
        'text': 1,
        'img': 2,
        'audio': 3,
        'video': 4,
        'img_and_text': 10
    }

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = None
        self.token = None
        if password:
            self.password = hashlib.md5(password).hexdigest()

    def login(self):
        """
        强制重新登录，不论是否曾经登录过
        """
        if not self.email:
            self.email = settings.wx_email
        if not self.password:
            self.password = hashlib.md5(settings.wx_password).hexdigest()
        body = self.gen_body('login')
        self.opener = poster.streaminghttp.register_openers()
        self.cookie = cookielib.CookieJar()
        self.opener.add_handler(
            urllib2.HTTPCookieProcessor(self.cookie))
        self.opener.addheaders = settings.wx_header
        try:
            msg = json.loads(self.opener.open(
                settings.wx_login_url, urllib.urlencode(body), timeout=5).read())
        except Exception as e:
            raise LoginException(e)
        if msg['ErrCode'] not in (0, 65202):
            raise LoginException(msg)
        self.token = msg['ErrMsg'].split('=')[-1]
        time.sleep(1)

    def login_unless_not(self):
        """
        登录如果曾经登陆过，则忽略此次登录操作
        """
        if not self.token:
            self.login()

    def gen_body(self, type, fake_id=None):
        body = {}
        if type == 'login':
            body['username'] = self.email
            body['pwd'] = self.password
            body['imgcode'] = ''
            body['f'] = 'json'
        elif type == 'push':
            body['error'] = 'false'
            body['token'] = self.token
            body['tofakeid'] = fake_id
            body['ajax'] = 1
        return body

    def send_txt_msg(self, send_to, msg):
        self.login_unless_not()
        data = {
            'type': self.push_msg_type['text'],
            'content': msg
        }

        self.opener.addheaders += [('Referer', settings.wx_send_msg_referer_url % str(send_to))]
        body = self.gen_body('push', send_to)
        body.update(data)
        try:
            msg = json.loads(self.opener.open(settings.wx_single_send_url, urllib.urlencode(body), timeout=5).read())
        except urllib2.URLError, e:
            logging.error(e.message, e)
            return False

        if msg['msg'] == 'ok':
            return True

    def get_contact_by_group(self, groupid=2):
        self.login_unless_not()
        self.opener.addheaders += [('Referer': settings.wx_index_url % self.token)]
        self.opener.open(settings.wx_contact_url % (self.token, settings.started))


class PushException(Exception):
    pass


class LoginException(Exception):
    pass

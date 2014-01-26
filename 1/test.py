#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Turbidsoul
# @Date:   2014-01-24 16:20:13
# @Last Modified by:   Turbidsoul
# @Last Modified time: 2014-01-26 11:17:42
import hashlib
import requests
from settings import weather3_url
from util import checkSignure, to_unicode, singleton


def test_receve_signature():
    headers = {
        "Content-Type": "application/xml"
    }

    xml = """<xml><ToUserName><![CDATA[gh_081abfe3962c]]></ToUserName>
    <FromUserName><![CDATA[oCT3bjgZ2GysH7vAz9sJK32DHZAs]]></FromUserName>
    <CreateTime>1363672441</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[subscribe]]></Event>
    <EventKey>aaaaaaaaaaaaaa</EventKey>
    </xml>"""

    timestamp = "12345678"
    nonce = "1234"
    token = "wxturbidsoul"
    echostr = "test"
    args = [timestamp, nonce, token]
    args.sort()
    signature = hashlib.sha1("".join(args)).hexdigest()
    url = "http://localhost:8080/?timestamp=" + timestamp + "&nonce=" + nonce + "&echostr=" + echostr + "&signature=" + signature
    response = requests.get(url, data=xml, headers=headers)
    assert response.text == 'test'


def test_receve_textmsg():
    headers = {
        "Content-Type": "application/xml"
    }

    xml = """<xml><ToUserName><![CDATA[gh_081abfe3962c]]></ToUserName>
    <FromUserName><![CDATA[oCT3bjgZ2GysH7vAz9sJK32DHZAs]]></FromUserName>
    <CreateTime>1363672441</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content>时间</Content>
    <MsgId>1234567890123456</MsgId>
    </xml>"""

    timestamp = "12345678"
    nonce = "1234"
    token = "wxturbidsoul"
    args = [timestamp, nonce, token]
    args.sort()
    signature = hashlib.sha1("".join(args)).hexdigest()
    url = "http://localhost:8080/?timestamp=" + timestamp + "&nonce=" + nonce + "&signature=" + signature
    response = requests.post(url, data=xml, headers=headers)
    assert response.status_code == 200


def test_xinzhi_weather_api():
    f = open('weathercity.code.txt', 'rb')
    wc = f.read()
    wcmap = {}
    wcmap = dict([tuple(code.split(',')) for code in wc.split('|') if len(code.split(',')) == 2])
    assert wcmap['陕西西安'] == '101110101'
    response = requests.get(weather3_url % wcmap['陕西西安'])
    assert response.status_code == 200


def test_checkSignure():
    assert not checkSignure('abcd', '1371630815', 'asdfasd', 'asdf')
    assert checkSignure('abcd', '1371630815', 'asdfasd', '272aeed372eb37fb01b49784e48f561fb670046d')


def test_to_unicode():
    assert to_unicode("123") == u'123'
    assert to_unicode('abc') == u'abc'
    assert to_unicode("测试") == u'\u6d4b\u8bd5'


def test_singleton():
    @singleton
    class Test(object):
        pass

    class Test2(object):
        pass

    t1 = Test()
    t2 = Test()
    assert t1 == t2

    t21 = Test2()
    t22 = Test2()
    assert not t21 == t22
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Turbidsoul
# @Date:   2014-01-24 16:20:13
# @Last Modified by:   Turbidsoul
# @Last Modified time: 2014-01-26 11:05:43
import hashlib
import requests
from settings import weather3_url

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


# coding: utf8
import httplib
import hashlib
import urllib


headers = {
    "Content-Type": "application/xml"
}

xml = """<xml>
<ToUserName><![CDATA[to user name]]</ToUserName>
<FromUserName><![CDATA[from user name]]</FromUserName>
<CreateTime>12345678</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[asdf]]></Content>
<MsgId>123456788</MsgId></xml>"""
xml = urllib.urlencode(xml)

timestamp = "12345678"
nonce = "1234"
token = "wxturbidsoul"
echostr = "test"
args = [timestamp, nonce, token]
args.sort()
signature = hashlib.sha1("".join(args)).hexdigest()
url = "?timestamp=" + timestamp + "&nonce=" + nonce + "&echostr=" + echostr + "&signature=" + signature
conn = httplib.HTTPConnection(host="127.0.0.1", port=8080)
conn.request(method='POST', url=url, body=xml, headers=headers)
response = conn.getresponse()
print response.read()
conn.close()

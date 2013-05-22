# coding: utf8
import hashlib
import httplib
import settings
import push


def test_receve_msg():
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
    url = "?timestamp=" + timestamp + "&nonce=" + nonce + "&echostr=" + echostr + "&signature=" + signature
    conn = httplib.HTTPConnection(host="127.0.0.1", port=8080)
    conn.request(method='POST', url=url, body=xml, headers=headers)
    response = conn.getresponse()
    print response.read()
    conn.close()


def test_push_msg():
    p = push.Push(settings.email, settings.password)
    p.login()
    print(p.token)
    result = p.send_txt_msg('5636455', '测试测试推送消息')
    print("推送成功" if result else "推送失败")

test_push_msg()

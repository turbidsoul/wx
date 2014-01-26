# coding: utf8

import time
from util import to_unicode


class Reply(object):
    """回复消息基类"""
    def __init__(self, touser, fromuser, func_flag):
        self.touser = touser
        self.fromuser = fromuser
        self.create_time = int(time.time())
        self.func_flag = func_flag

    def to_xml(self):
        '''生成XML字符串'''
        pass


class TextReply(Reply):
    """回复文本消息"""

    xml_template = '''<xml>
<ToUserName>%s</ToUserName>
<FromUserName>%s</FromUserName>
<CreateTime>%s</CreateTime>
<MsgType>%s</MsgType>
<FuncFlag>%s</FuncFlag>
<Content>%s</Content></xml>'''

    def __init__(self, touser, fromuser, func_flag, content):
        super(TextReply, self).__init__(touser, fromuser, func_flag)
        self.msg_type = "text"
        self.content = content

    def to_xml(self):
        args = (
            self.touser,
            self.fromuser,
            self.create_time,
            self.msg_type,
            0,
            to_unicode(self.content)
        )
        return self.xml_template % args


class MusicReply(Reply):
    """回复音乐消息"""

    xml_template = '''<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%d</CreateTime>
<MsgType><![CDATA[%s]]></MsgType>
<Music>
<Title><![CDATA[%s]]></Title>
<Description><![CDATA[%s]]></Description>
<MusicUrl><![CDATA[%s]]></MusicUrl>
<HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
</Music>
<FuncFlag>%d</FuncFlag>
</xml>'''

    def __init__(self, touser, fromuser, func_flag, music_title, music_url, music_hq_url, music_description):
        super(TextReply, self).__init__(touser, fromuser, func_flag)
        self.music_url = music_url
        self.music_hq_url = music_hq_url
        self.music_title = music_title
        self.music_description = music_description
        self.msg_type = "music"

    def to_xml(self):
        args = (
            self.tosuer,
            self.fromuser,
            self.create_time,
            self.msg_type,
            to_unicode(self.music_title),
            to_unicode(self.music_description),
            self.music_url,
            self.music_url,
            self.music_hq_url,
            self.func_flag
        )
        return self.xml_template % args


class Article(object):
    """Article"""

    xml_template = '''<item>
 <Title><![CDATA[%s]]></Title>
 <Description><![CDATA[%s]]></Description>
 <PicUrl><![CDATA[picurl]]></PicUrl>
 <Url><![CDATA[url]]></Url>
 </item>'''

    def __init__(self, title, description, pic_url, url):
        super(Article, self).__init__()
        self.title = title
        self.description = description
        self.pic_url = pic_url
        self.url = url

    def to_xml(self):
        return self.xml_template % (self.title, self.description, self.pic_url, self.url)


class ArticleReply(Reply):
    """回复图文消息"""

    xml_template = """<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%d</CreateTime>
<MsgType><![CDATA[%s]]></MsgType>
<ArticleCount>%d</ArticleCount>
<Articles>
%s
</Articles>
<FuncFlag>%s</FuncFlag>
</xml>"""

    def __init__(self, touser, fromuser, count, articles, func_flag):
        super(ArticleReply, self).__init__(touser, fromuser, func_flag)
        self.count = int(count)
        self.articles = articles
        self.msg_type = 'news'

    def to_xml(self):
        articles_xml = ""
        for a in self.articles:
            articles_xml += a.to_xml()
        args = (
            self.touser,
            self.fromuser,
            self.create_time,
            self.msg_type,
            self.count,
            articles_xml,
            0
        )
        return self.xml_template % args


def _now():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def _today():
    return time.strftime('%Y-%m-%d')

def _time():
    return time.strftime('%H:%M:%S')


def generate_reply(msg):
    args = dict(
        touser=msg.fromuser,
        fromuser=msg.touser,
        func_flag=0
    )
    if msg.msg_type == 'text':
        args['content'] = "溺社撒！？"
        if msg.content.strip() == 'datetime' or msg.content.strip().encode('utf8') == "时间":
            args['content'] = _now()
        elif msg.content.strip() == 'date':
            args['content'] = _today()
        elif msg.content.strip() == 'time':
            args['content'] = _time()
        return TextReply(**args)
    if msg.msg_type == "event":
        if msg.event == "subscribe":
            args['content'] = "欢迎关注俺，俺是个机器人！"
            return TextReply(**args)
        elif msg.event == "unsubscribe":
            pass
        elif msg.event == "CLICK":
            pass
    return

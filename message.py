# coding: utf8

import xml.etree.cElementTree as et
import logging
from util import to_unicode


class Message(object):
    """Wei chart super class"""
    def __init__(self, touser, fromuser, create_time, msg_id):
        self.touser = touser
        self.fromuser = fromuser
        self.create_time = int(create_time)
        if msg_id:
            self.msg_id = int(msg_id)


class TextMessage(Message):
    """
    Text message

    touser - 开发者微信号

    fromuser - 发送方微信号（OpenId）

    create_time - 消息创建时间

    msg_id - 消息Id，64位整数

    content - 文本消息内容
    """
    def __init__(self, touser, fromuser, create_time, msg_id, content):
        super(TextMessage, self).__init__(touser, fromuser, create_time, msg_id)
        self.content = content
        if self.content == 'Hello2BizUser':
            self.msg_type = 'hello'
        self.msg_type = "text"


class ImageMessage(Message):
    """
    Image message

    pic_url - 图片连接
    """
    def __init__(self, touser, fromuser, create_time, msg_id, pic_url):
        super(ImageMessage, self).__init__(touser, fromuser, create_time, msg_id)
        self.msg_type = "image"
        self.pic_url = pic_url


class LinkMessage(Message):
    """
    Link message

    title - 消息标题

    description - 消息描述

    url - 消息链接
    """
    def __init__(self, touser, fromuser, create_time, msg_id, title, description, url):
        super(LinkMessage, self).__init__(touser, fromuser, create_time, msg_id)
        self.msg_type = "link"
        self.title = title
        self.description = description
        self.url = url


class LocationMessage(Message):
    """
    Location Message

    x - 地理位置纬度

    y - 地理位置经度

    scale - 地图缩放大小

    label - 地理位置信息
    """
    def __init__(self, touser, fromuser, create_time, msg_id, x, y, scale, label):
        super(LocationMessage, self).__init__(touser, fromuser, create_time, msg_id)
        self.msg_type = "location"
        self.x = x
        self.y = y
        self.scale = scale
        self.label = label


class EventMessage(Message):
    """
    Event push message

    event - 事件类型，有subscribe(订阅), unsubscribe(取消订阅)， CLICK(自定义菜单点击事件)

    event_key - 时间Key值，对应自定义菜单中的Key
    """
    def __init__(self, touser, fromuser, create_time, msg_id, event, event_key):
        super(EventMessage, self).__init__(touser, fromuser, create_time, msg_id)
        self.msg_type = "event"
        self.event = event
        self.event_key = event_key


class ErrorMessage(object):
    """错误消息"""
    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg


def parse_message(xml):
    '''Parse from weixin receive xml to message '''
    if not xml:
        return
    logging.info(xml)
    root = et.fromstring(xml)
    _msg = dict(
        touser=root.find('ToUserName').text,
        fromuser=root.find('FromUserName').text,
        create_time=root.find('CreateTime').text
    )
    msg_type = root.find('MsgType').text
    if msg_type == 'text':
        _msg['content'] = to_unicode(root.find('Content').text)
        _msg['msg_id'] = root.find('MsgId').text
        return TextMessage(**_msg)
    elif msg_type == 'image':
        _msg['pic_url'] = root.find('PicUrl').text
        _msg['msg_id'] = root.find('MsgId').text
        return ImageMessage(**_msg)
    elif msg_type == 'location':
        _msg['x'] = root.find('Location_x').text
        _msg['y'] = root.find('Location_y').text
        _msg['scale'] = root.find('Scale').text
        _msg['label'] = to_unicode(root.find('Label').text)
        _msg['msg_id'] = root.find('MsgId').text
        return LocationMessage(**_msg)
    elif msg_type == 'link':
        _msg['title'] = to_unicode(root.find('Title').text)
        _msg['description'] = to_unicode(root.find('Description').text)
        _msg['url'] = root.find('Url').text
        _msg['msg_id'] = root.find('MsgId').text
        return LinkMessage(**_msg)
    elif msg_type == 'event':
        _msg['event'] = root.find('Event').text
        _msg['event_key'] = root.find('EventKey').text
        _msg['msg_id'] = None
        return EventMessage(**_msg)

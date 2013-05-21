# coding: utf8

from hashlib import sha1
from message import TextMessage, ImageMessage, LinkMessage, LocationMessage, EventMessage
import xml.etree.cElementTree as et
import logging


def checkSignure(token, timestamp, nonce, signature):
    '''check signature'''
    args = [token, timestamp, nonce]
    args.sort()
    return sha1("".join(args)).hexdigest() == signature


def to_unicode(value):
    if isinstance(value, unicode):
        return value
    if isinstance(value, basestring):
        return value.decode('utf-8')
    if isinstance(value, int):
        return str(value)
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value


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

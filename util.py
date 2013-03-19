# coding: utf8

from hashlib import sha1
from message import TextMessage
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


def parse_messsage(xml):
    '''Parse from weixin receive xml to message '''
    if not xml:
        return
    logging.info(xml)
    root = et.fromstring(xml)
    _msg = dict(
        touser=root.find('ToUserName').text,
        fromuser=root.find('FromUserName').text,
        create_time=root.find('CreateTime').text,
        msg_id=root.find('MsgId').text
    )
    if root.find('MsgType').text == 'text':
        _msg['content'] = to_unicode(root.find('Content').text)
        return TextMessage(**_msg)
    else:
        return

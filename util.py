# coding:utf8

from hashlib import sha1
from message import TextMessage
import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element, SubElement
from time import time
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

    root = et.fromstring(xml.decode('utf8'))
    _msg = dict(
        touser=root.find('ToUserName').text,
        fromuser=root.find('FromUserName').text,
        create_time=root.find('CreateTime').text,
        msg_type=root.find('MsgType').text,
        msg_id=root.find('MsgId')
    )
    if _msg['msg_type'] == 'text':
        logging.info(root.find('Content').text)
        _msg['content'] = root.find('Content').text
        return TextMessage(**_msg)
    else:
        return


def generate_reply(msg):
    '''generate reply xml'''
    root = Element('xml')
    touser = SubElement(root, 'ToUserName')
    touser.text = msg.fromuser
    fromuser = SubElement(root, 'FromUserName')
    fromuser.text = msg.touser
    createtime = SubElement(root, 'CreateTime')
    t = str(time())
    t = t[:len(t) - 3]
    createtime.text = t
    msgtype = SubElement(root, 'MsgType')
    msgtype.text = msg.msg_type
    funcflag = SubElement(root, 'FuncFlag')
    funcflag.text = '0'
    if msg.msg_type == 'text':
        content = SubElement(root, 'Content')
        content.text = msg.content
    return et.tostring(root)

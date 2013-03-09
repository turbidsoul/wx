# coding:utf8

from hashlib import sha1
from message import TextMessage
import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element, SubElement
from time import time


def checkSignure(token, timestamp, nonce, signature):
    '''check signature'''
    args = [token, timestamp, nonce]
    args.sort()
    return sha1("".join(args)).hexdigest() == signature


def parse_messsage(xml):
    '''Parse from weixin receive xml to message '''
    if not xml:
        return

    msg = dict((c.tag, c.text.decode('utf-8')) for c in et.fromstring(xml))
    _msg = dict(
        touser=msg['ToUserName'] or 'none',
        fromuser=msg['FromUserName'],
        create_time=msg['CreateTime'],
        msg_type=msg['MsgType'],
        msg_id=msg['MsgId']
    )
    if _msg['msg_type'] == 'text':
        _msg['content'] = msg.get('Content')
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
        content.text = msg.content.decode('utf8')
    return et.tostring(root)

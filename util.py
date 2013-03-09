# coding:utf8

from hashlib import sha1
import xml.etree.ElementTree as et


def checkSignure(token, timestamp, nonce, signature):
    '''check signature'''
    args = [token, timestamp, nonce]
    args.sort()
    return sha1("".join(args)).hexdigest() == signature


def parse_messsage(xml):
    tree = et.ElementTree(xml)

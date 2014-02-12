# -*- coding: utf8 -*-

from hashlib import sha1


def checkSignure(token, timestamp, nonce, signature):
    '''
    check signature
    '''
    args = [token, timestamp, nonce]
    args.sort()
    return sha1("".join(args)).hexdigest() == signature


def to_unicode(value):
    """
    convert string to unicode
    """
    if isinstance(value, unicode):
        return value
    if isinstance(value, basestring):
        return value.decode('utf-8')
    if isinstance(value, int):
        return str(value)
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value


def singleton(cls, *args, **kw):
    """
    单例

    """
    instances = {}

    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance




# -*- coding: utf8 -*-

from hashlib import sha1


def checkSignure(token, timestamp, nonce, signature):
    '''
    check signature

    >>> checkSignure('abcd', '1371630815', 'asdfasd', 'asdf')
    False
    >>> checkSignure('abcd', '1371630815', 'asdfasd', '272aeed372eb37fb01b49784e48f561fb670046d')
    True
    '''
    args = [token, timestamp, nonce]
    args.sort()
    return sha1("".join(args)).hexdigest() == signature


def to_unicode(value):
    """
    convert string to unicode

    >>> to_unicode("123")
    u'123'
    >>> to_unicode("abc")
    u'abc'
    >>> to_unicode("测试")
    u'\u6d4b\u8bd5'
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

    @singleton
    class ClassName(object):
        pass
    """
    instances = {}

    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

if __name__ == '__main__':
    import doctest
    doctest.testmod()

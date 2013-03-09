# coding: utf8
#
#
#
#
#


class Message(object):
    """Wei chart super class"""
    def init(self):
        pass


class TextMessage(Message):
    """Text message"""
    def __init__(self, touser, fromuser, create_time, msg_type, msg_id, content):
        self.touser = touser
        self.fromuser = fromuser
        self.create_time = create_time
        self.msg_type = msg_type
        self.msg_id = msg_id
        self.content = content
        if self.content == 'Hello2BizUser':
            self.msg_type = 'hello'

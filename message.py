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
    def __init__(self, to, from, create_time, msg_type, content, msg_id):
        super(TextMessage, self).__init__()
        self.to = to
        self.from = from
        self.create_time = create_time
        self.msg_type = msg_type
        self.content = content
        self.msg_id = msg_id

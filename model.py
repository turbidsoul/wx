# coding: utf8

#*********************************************************#
# @@ScriptName: model.py
# @@Author: Turbidsoul Chen<sccn.sq@gmail.com>
# @@Create Date: 2013-04-16 16:19:37
# @@Modify Date: 2013-04-16 16:33:25
# @@Function:
#*********************************************************#


from google.appengine.ext import db


class WXUser(db.Model):
    """
    微信用户
    """

    nickname = db.StringProperty()
    fake_id = db.StringProperty()
    user_name = db.StringProperty()
    remark_name = db.StringProperty()
    signature = db.StringProperty()
    country = db.StringProperty()
    province = db.StringProperty()
    city = db.StringProperty()
    sex = db.IntegerProperty(default=0, choices=[0, 1, 2])
    group_id = db.IntegerProperty()
    group_name = db.StringProperty()
    create_date = db.DateTimeProperty(auto_now_add=True)
    sync_date = db.DateTimeProperty(auto_now=True)
    follow_date = db.DateTimeProperty(auto_now_add=True)
    unfollow_date = db.DateTimeProperty()

    def save(self):
        self.put()

# -*- coding: utf8 -*-
import webapp2
from push import Push
import settings
import time
from model import WXUser
import json
import poster
import logging
from util import to_unicode


class TestTaskWorker(webapp2.RequestHandler):

    """
    test task
    """
    def get(self):
        p = Push(settings.wx_email, settings.wx_password)
        p.login()
        p.send_txt_msg("5636455", time.strftime('%Y-%m-%d %H:%M:%S'))


class WeatherTaskWorker(webapp2.RequestHandler):

    """
    天气预报提醒
    """
    def get(self):
        users = WXUser.all()
        p = Push()
        if not users.count():
            return
        opener = poster.streaminghttp.register_openers()
        weatherinfo = json.loads(opener.open(settings.weather1_url % settings.weather_city, timeout=5).read())['weatherinfo']
        logging.info(weatherinfo)
        city = weatherinfo['city']
        temp = weatherinfo['temp']
        wd = weatherinfo['WD']
        ws = weatherinfo['WS']
        sd = weatherinfo['WS']
        time = weatherinfo['time']
        args = (to_unicode(city), temp, to_unicode(wd), to_unicode(ws), sd, time)
        logging(str(args))
        for user in users:
            msg = '''
城市：%s
温度：%s 摄氏度
风向：%s
风力：%s
湿度：%s
发布时间：%s''' % (to_unicode(city), temp, to_unicode(wd), to_unicode(ws), sd, time)
            logging.info(msg)
            p.send_txt_msg(user.fake_id, msg)


class SyncUserTaskWorker(webapp2.RequestHandler):
    """
    同步用户
    """
    def get(self):
        p = Push()
        p.login_unless_not()
        p.get_contact_by_group()


app = webapp2.WSGIApplication([
    ('/task/test', TestTaskWorker),
    ('/task/weather', WeatherTaskWorker),
    ('/task/syncuser', SyncUserTaskWorker)
], debug=True)

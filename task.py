# -*- coding: utf8 -*-
import webapp2
from push import Push
import settings


class TestTaskWorker(webapp2.RequestHandler):
    """
    test task
    """
    def get(self):
        p = Push(settings.email, settings.password)
        p.login()
        p.send_txt_msg("5636455", "定时发送")


app = webapp2.WSGIApplication([('/task/test', TestTaskWorker)], debug=True)

# -*- coding: utf8 -*-
import webapp2
from push import Push
import settings
import time


class TestTaskWorker(webapp2.RequestHandler):
    """
    test task
    """
    def get(self):
        p = Push(settings.email, settings.password)
        p.login()
        p.send_txt_msg("5636455", time.strftime('%Y-%m-%d %H:%M:%S'))


app = webapp2.WSGIApplication([('/task/test', TestTaskWorker)], debug=True)

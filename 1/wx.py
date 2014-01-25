#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging
from util import checkSignure, to_unicode
from reply import generate_reply
from message import parse_message

token = 'wxturbidsoul'


class WXChartHandler(webapp2.RequestHandler):
    def get(self):
        global token
        signature = self.request.get('signature')
        timestamp = self.request.get('timestamp')
        nonce = self.request.get('nonce')
        echostr = self.request.get('echostr')
        if checkSignure(token, timestamp, nonce, signature):
            logging.info("connection wx rebot success")
            self.response.write(echostr)
        else:
            logging.info("connection wx rebo fail")
            webapp2.abort(403)

    def post(self):
        global token
        _args = dict(
            token=token,
            timestamp=self.request.get('timestamp'),
            nonce=self.request.get('nonce'),
            signature=self.request.get('signature')
        )
        if not checkSignure(**_args):
            return webapp2.abort(403)
        message = parse_message(self.request.body)
        reply = generate_reply(message)
        self.response.content_type = 'application/xml'
        self.response.write(to_unicode(reply.to_xml()))

app = webapp2.WSGIApplication([('/', WXChartHandler)], debug=True)

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
import logging

from bottle import abort, default_app, error, request, route, response
from settings import token
from util import checkSignure, to_unicode

from reply import generate_reply
from message import parse_message



# class WXChartHandler(webapp2.RequestHandler):
#     def get(self):
#         global token
#         signature = self.request.get('signature')
#         timestamp = self.request.get('timestamp')
#         nonce = self.request.get('nonce')
#         echostr = self.request.get('echostr')
#         if checkSignure(token, timestamp, nonce, signature):
#             logging.info("connection wx rebot success")
#             self.response.write(echostr)
#         else:
#             logging.info("connection wx rebo fail")
#             webapp2.abort(403)

#     def post(self):
#         global token
#         _args = dict(
#             token=token,
#             timestamp=self.request.get('timestamp'),
#             nonce=self.request.get('nonce'),
#             signature=self.request.get('signature')
#         )
#         if not checkSignure(**_args):
#             return webapp2.abort(403)
#         message = parse_message(self.request.body)
#         reply = generate_reply(message)
#         self.response.content_type = 'application/xml'
#         self.response.write(to_unicode(reply.to_xml()))


@route('/', method='GET')
def wx_signature():
    params = request.params
    signature = params['signature']
    timestamp = params['timestamp']
    nonce = params['nonce']
    echostr = params['echostr']
    if not signature or not timestamp or not nonce or not echostr:
        logging.error('check signature failed')
        abort(403, 'check siginure failed')
    if checkSignure(token, timestamp, nonce, signature):
        logging.info("connection wx rebot success")
        return echostr
    else:
        logging.info("connection wx rebot fail")
        abort(403, 'connection wx rebot fail')


@route('/', method='POST')
def wx_message():
    params = request.params
    signature = params['signature']
    timestamp = params['timestamp']
    nonce = params['nonce']
    _args = {
        "token": token,
        "signature": signature,
        "timestamp": timestamp,
        "nonce": nonce
    }
    if not signature or not timestamp or not nonce:
        logging.error('check signature failed')
        abort(403, 'check siginure failed')
    if not checkSignure(**_args):
        abort(403)
    print(request.body.getvalue())
    message = parse_message(request.body.getvalue())
    reply = generate_reply(message)
    response.set_header("Content-Type", 'application/xml')
    return to_unicode(reply.to_xml())


@route('/hello')
@route('/hello/')
@route('/hello/:name')
def hello(name=None):
    print(name)
    if name:
        return "hello %s !" % name
    abort(403)


@error(403)
def error_403(error):
    return "403"


app = default_app()

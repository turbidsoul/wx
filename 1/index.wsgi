


import sae


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello, world!']


application = sae.create_wsgi_app(app)
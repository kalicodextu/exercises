import falcon

from gevent.wsgi import WSGIServer
from gevent import monkey

import settings

from apps import handlers
from application import Application

monkey.patch_all()

class RequireJson(object):
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON')
        if req.method in ('POST','PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.')

if __name__ == "__main__":
    config = settings.config
    logger = settings.logger
    settings = dict(middleware=[RequireJson()])
    app = Application(handlers, config, **settings)

    logger.info('start listen on %s' % config['api_port'])
    WSGIServer(('', config['api_port']), app, log=logger).serve_forever()


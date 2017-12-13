import falcon
import json

from base import BaseHandler
from xybase.utils.encryption_base import create_hash_key, create_md5_key
from settings import logger


class Account(BaseHandler):
    def on_get(self, req, resp, account_id):
        flag, account = self.storage.search_by_id('accounts', account_id)
        account.pop('password', None)
        if account:
            resp.body = json.dumps(account)
            resp.status = falcon.HTTP_200
            return
        else:
            resp.status = falcon.HTTP_404
            return

    def on_put(self, req, resp, account_id):
        data = json.loads(req.stream.read())
        result =self.storage.update('accounts', account_id, data)
        if result:
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_200
            return
        else:
            resp.status = falcon.HTTP_500
            logger.error('account PUT internal error')
            return

class ChangePassword(BaseHandler):
    def on_post(self, req, resp, account_id):
        data = json.load(req.stream)
        flag, account = self.storage.search_by_id('accounts', account_id)
        if flag:
            if account:
                mobile = account.get('mobile')
                secret_key = create_md5_key(account['id'])
            else:
                resp.status = falcon.HTTP_400
                logger.error('The result is empty!')
                return
        else:
            resp.status = falcon.HTTP_500
            return

        if not mobile:
            resp.status, resp.body = self.result_error(
                self.ERROR_MSG['no_mobile_info'])
            return
        

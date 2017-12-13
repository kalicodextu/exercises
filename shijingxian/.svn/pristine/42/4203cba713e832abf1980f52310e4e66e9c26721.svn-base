class AccountsPatchingWechatID(BaseHandler):
    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        flag, tag = self.check_sms_code(
            data['mobile'], self.REDIS_STRING['wbv'], data['smsCode'])
        if not flag:    #check_sms_code failed
            resp.status, resp.body = self.result_error(tag)
            return
        account = self.storage.search_by_condition('accounts',
                                                   {'mobile': data['mobile']})
        condition = dict()
        if not account:
            condition['mobile'] = data['mobile']
            condition['wechatId'] = data['wechatId']
            condition['type'] = 'family'
            result = self.storage.create('accounts', condition)
        else:
            if account[0].get('wechatId'):
                resp.status, resp.body = self.result_error(
                    self.ERROR_MSG['conflict_info_exist'])
                return

            #sjx code start
            wechat_account = self.storage.search_by_condition('accounts',{'wecharId':data['wechatId']})
            if wechat_account[0].get('wechatId'):
                resp.status, resp.body = self.result_error(
                    self.ERROR_MSG['conflict_info_exist'])
                return
            #sjx code end

            condition['wechatId'] = data['wechatId']
            account_id = account[0]['id']
            result = self.storage.update('accounts', account_id, condition)

        if result:
            resp.status = falcon.HTTP_201
            resp.body = json.dumps(result)
            return
        else:
            resp.status = falcon.HTTP_500
            return



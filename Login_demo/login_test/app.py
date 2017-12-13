import falcon
import sign_up
import login
import psw_edit

api = application = falcon.API()
api.add_route('/login',login.Resource())
api.add_route('/sign-up',sign_up.Resource())
api.add_route('/psw-edit',psw_edit.Resource())

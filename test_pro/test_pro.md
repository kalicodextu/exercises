#一 guardians

## authorization

1. guardian-session
	* guardian的登录,可以使用以下方式登录:
		* name-password
		* mobile-password
		* mobile-smscode
		* ~~wechatid~~
	* need
		* name password
		* mobile password
		* mobile smscode
	* return (some of)
		* mobile
		* token
		* type
		* id(guardianId)
		* name
	* status-code
		* 201
	
* guardians
	* guardian的注册,可以使用以下方式注册
		* name, password, imgCode, uuid, type
		* mobile, password, smsCode, type
	* relation
		* name
			*image-code*
		* mobile
			*smscode*
	* need
		* name password  imgCode  uuid  type
		* mobile  password  smsCode  type
	* return 
		id(guardianId)
	* status_code
		* 200
	* remark
		*个人注册默认`type`为`family`*

* guardians-patch-wechat-id
	*~~NOT USE~~*
	
* guardians-reset-password
	* guardian忘记密码时使用
	* relation
		*需要事前绑定手机号,之后可以使用短信验证码,重设密码*
	* need
		* mobile
		* newPassword
		* smsCode
	* return
		* id(guardianId)
	* status_code
		* 200
	
* guardians-sms
	* guardian发送验证码时的内部服务,可以用来:
		* 注册(sign_up)
		* 登录(sign_in)
		* 重设密码(forget_password)
		* 绑定手机号(mobile_binding)
		* ~~绑定微信(wechat_binding)~~
	* need
		* mobile
		* verifyType
		* uuid
	* return
		* uuid
	* status_code
		* 200
		
* guardians-guardianId-sms
	* guardian登录后使用手机发送验证码时的内部服务,可以用来:
		* 修改密码(change_password)
		* 解绑手机(mobile_releasing)
	* need
		* verifyType
	* return
		* id
	* status_code
		* 200
		
* guardians-guardianId-binding-mobile
	* guardian绑定手机号
	* relation
		* 登录(guardian-sessions)
		* 发送绑定短信(guardians-sms)
	* need
		* mobile
		* smsCode
	* return 
		* id(guardianId)
	* status_code
		* 200
		
* change-name
	* 使用手机号注册guardian账户后,首次修改用户名
	* relation
		* 登录(guardian-sessions)
	* need
		* name
	* return
		* id(guardianId)
	* status_code
		* 200
	* remark
		*只能修改一次, 如果使用`name-password`方式注册,则不能使用*
	
* change-password
	* guardian 修改密码
	* relation
		* 登录(guardian-sessions)
		* 发送修改密码短信(guardians-guardianId-sms)
	* need
		* smsCode
		* newPassword
		* oldPassword
	* return
		* id(guardianId)
	* status_code
		* 200

* release-mobile
	* guardian 解绑手机
	* relation
		* 登录(guardian-sessions)
		* 发送解绑手机短信(guardians-guardianId-sms)
	* need
		* smsCode
	* return
		* id(guardianId)
	* status_code
		* 200
		

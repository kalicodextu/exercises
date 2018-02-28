* guardian-session (login)

``` python
{
    "name" : "guardian-session",
    "url" : "/authorization/guardian-sessions",
    "input_data" : {
        "valid" : {
            "mobile_password" : {
                "password" : "123456",
                "mobile" : "13333333333"
            },
            "mobile_smscode" : {
                "smscode" : "1609",
                "mobile" : "13333333333"
            },
            "name" : {
                "name" : "testguardian",
                "password" : "123456"
            },
            "wechatId" : {
                "wechatId" : "wechatid"
            }
        },
        "invalid" : {}
    },
    "output_data" : {
        "type" : "org"
    }
}
```

* guardians (sign-up)

``` python
{
    "name" : "guardians",
    "url" : "/authorization/guardians",
    "input_data" : {
        "valid" : {
            "mobile" : {
                "password" : "123456",
                "mobile" : "13333333333",
                "smscode": "1609",
                "type": "org"
            },
            "name" : {
                "name" : "testguardian",
                "password" : "123456",
                "imgCode": "temp",
                "type": "org",
                "uuid": "123455666"
            },
        },
        "invalid" : {}
    }{
    
}
}
```

* guardians/patch-wechat-id

``` python
{
    "name" : "guardians-patch-wechat-id",
    "url" : "/authorization/guardians/patch-wechat-id",
    "input_data" : {
        "valid" : {},
        "invalid" : {}
    }
}
```

* guardians/reset-password

``` python
{
    "name": "guardians-reset-password",
    "url": "/authrozation/guardians/reset-password",
    "input_data": {
        "valid": {
            "mobile": "13333333333",
            "smscode": "1609",
            "newPassword": "123456789"
        },
        "invalid": {
            
        }
    },
    "output_data": {}
}
```

* guardians/sms

``` python
{
    "name" : "guardians-sms",
    "url" : "/authorization/guardians/sms",
    "input_data" : {
        "valid" : {
            "sign_up": {
                "mobile": "13333333333", 
                "uuid": "123455666",
                "verifyType": "sign_up"
            },
            "sign_in": {                  
                "mobile": "13333333333", 
                "uuid": "123455666",
                "verifyType": "sign_in"
            },
            "forget_password": {                  
                "mobile": "13333333333", 
                "uuid": "123455666",
                "verifyType": "forget_password"
            },
            "mobile_binding": {                  
                "mobile": "13333333333", 
                "uuid": "123455666",
                "verifyType": "mobile_binding"
            },
            "wechat_binding": {                  
                "mobile": "13333333333", 
                "uuid": "123455666",
                "verifyType": "wechat_binding"
            }
        },                           
        "invalid" : {}
    },
    "output_data" : {
        "uuid" : "123455666"
    }
}
```

* guardians/guardianId/bind-mobile

``` python
{
    "name" : "guardians-bind-mobile",
    "url" : "/authorization/guardians/guardianId/bind-mobile",
    "input_data" : {
        "valid" : {
            "mobile": "13333333333", 
            "smsCode": "1609"
        },
        "invalid" : {}
    },
    "output_data" : {
        "uuid" : "123455666"
    }
}
```

* guardians/guardianId/change-name

``` python
{
    "name": "guardians-change-name",
    "url": "/authorization/guardians/guardianId/change-name",
    "input_data": {
        "valid": {
            "name":{
                "new_name": "testNewName",
                "origin_name": "testguardian"
            }
        }
    }
}
```

* guardians/guardianId/change-password

``` python
{
    "name": "guardians-change-password",
    "url": "/authorization/guardians/guardianId/change-password",
    "input_data": {
        "valid": {
            "new":{
                "newPassword": "123456789",
                "oldPassword": "123456"
            },
            "origin":{
                "newPassword": "123456",
                "oldPassword": "12345678"
            }
        },
        "invalid":{}
    }

}
```

* guardians/guardianId/release-mobile

``` python
{
    "name": "guardians-release-mobile",
    "url": "/authorization/guardians/guardianId/release-mobile",
    "input_data": {
        "valid": {
            "smsCode": "1609"    
        },
        "invalid":{
            "smsCode": "Fake"
        }
    }

}
```

* guardians/guardianId/sms

``` python
{
    "name": "guardians-guardianId-sms",
    "url": "/authorization/guardians/guardianId/sms",
    "input_data": {
        "valid": {
            "mobile_releasing": {
                "verifyType": "mobile_releasing"
            },
            "change_password": {
                "verifyType": "change_password"
            }
        }
    },
    "output_data": {
    }
}



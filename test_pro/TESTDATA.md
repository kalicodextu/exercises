# guardian
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
            "mobile_smsCode" : {
                "smsCode" : "1609",
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
        "type" : "family",
        "name" : "testguardian",
        "mobile": "13333333333"
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
                "smsCode": "1609",
                "type": "family"
            },
            "name" : {
                "name" : "testguardian",
                "password" : "123456",
                "imgCode": "temp",
                "type": "family",
                "uuid": "123455666"
            },
        },
        "invalid" : {}
    },
    "output_data" : {}
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
            "smsCode": "1609",
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
    "output_data" : {}
}
```

* guardians/guardianId/change-name

``` python
{
    "name": "guardians-change-name",
    "url": "/authorization/guardians/guardianId/change-name",
    "input_data": {
        "valid": {
            "name": "testguardian"
        }
    },
    "output_data": {}
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
                "oldPassword": "123456",
                "smsCode": "1609"
            },
            "origin":{
                "newPassword": "123456",
                "oldPassword": "12345678",
                "smsCode": "1609"
            }
        },
        "invalid":{}
    },
    "output_data": {}

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
```

# imgcode

* image-code

``` python
{
    "name": "image-code",
    "url": "/authorization/image-code",
    "input_data": {
        "valid": {
            "sign_up": {
                "verifyType": "sign_up",
                "uuid": "123455666"
            },
            "sign_in": {
                "verifyType": "sign_in",
                "uuid": "123455666"
            },
            "release_block_address": {
                "verifyType": "release_block_address",
                "uuid": "123455666"
            }
        }
    }
}
```

* image/uuid
``` python
{
    "name": "imgcode-uuid",
    "url": "/authorization/image-code/uuid",
    "input_data": {
        "valid": {
            "imgCode": "FAKE"
        },
        "invalid": {
            "imgCode": "FAKE"
        }
    },
    "output_data": {}
}
```

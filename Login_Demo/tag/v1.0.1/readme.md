# login_demo version:1.0.1
## 实现功能
简单的实现了登录管理的三个部分
> + 注册
> + 登录
> + 修改密码

## 操作步骤
> + 激活虚拟环境
> + python main.py
> + 在另一个 `terminal` 使用 `http` 进行请求
'''
1, http POST localhost:8000/signup Content-Type:text/json < test.json
2, http GET localhost:8000/signin Content-Type:text/json < test.json
3, http POST localhost:8000/chpw Content-Type:text/json < test.json
'''
将json file 定向到请求流中

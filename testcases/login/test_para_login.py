
"""登录的函数用参数化来解决"""
from api.login_func import login
import pytest
from utils.read_yml import read_yml
from pathlib import Path
import requests

p=Path(__file__)
yamlpath=p.parent.parent.parent.joinpath('data','data.yaml')
print(yamlpath)
test_data=read_yml(yamlpath)['login']

@pytest.mark.parametrize("test_input,expected",test_data
                    # [
                    #      [
                    #          {"user":"test1","password":"123456"} ,
                    #          {"code":0,"msg":"login success!"}
                    #      ],
                    #      [
                    #          {"user":"testaaa1","password":"123456"} ,
                    #          {"code":3003,"msg":"账号或密码不正确"}
                    #      ],
                    #      [
                    #          {"user":"test2","password":"123456x"} ,
                    #          {"code":3003,"msg":"账号或密码不正确"}
                    #      ],
                    #      [
                    #          {"user":"","password":""} ,
                    #          {"code":3003,"msg":"账号或密码不正确"}
                    #      ]
                    # ]
                    )

def test_login_params(test_input,expected):
    print("测试数据：",test_input)
    s = requests.Session()
    r=login(s,**test_input)
    #print(r.text)
    assert r.json()["code"]==expected["code"]
    assert r.json()["msg"]==expected["msg"]


"""
登录的四个用例
"""

from api.login_func import login
import requests
import pytest


def test_login_1():
    """输入正确的账号密码进行登录"""
    s=requests.Session()
    r=login(s)
    print("\n",r.text)
    assert r.json()["code"]==0
    assert r.status_code==200
    assert r.status_code<400
    assert r.status_code in [200,201]

def test_login_2():
    """输入未注册过的账号，登录失败"""
    s=requests.Session()
    r=login(s,username='xxyyqq',password='123456')
    print("\n",r.text)
    assert r.json()["code"]==3003
    assert r.json()['msg']=="账号或密码不正确"

def test_login_3():
    """输入错误的密码"""
    s=requests.Session()
    r=login(s,username='test1',password='1234567')
    print("\n",r.text)
    assert r.json()["code"]==3003
    assert r.json()['msg']=="账号或密码不正确"

def test_login_4():
    """输入空的账号密码"""
    s=requests.Session()
    r=login(s,username='',password='')
    print("\n",r.text)
    assert r.json()["code"]==3003
    assert r.json()['msg']=="账号或密码不正确"



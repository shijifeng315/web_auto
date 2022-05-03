from ke15.register_function import register
from ke15.conn import ConnectDB,db_info
import pytest

@pytest.fixture()
def delete_user():
    db=ConnectDB(db_info)
    #1.先删掉关联表的数据
    delete_sql = "delete from auth_user where username='test1xy';"
    res = db.select_sql(delete_sql)
    db.execute_sql(delete_sql)


def test_register_1():
    """注册成功的用例"""
    r=register(username='test1xy')
    print(r.json())
    assert r.json()['code']==0
    assert r.json()['msg']=='register success!'

def test_register_2():
    """重复注册"""
    r=register(username='test1xy')
    print(r.json())
    assert r.json()['code']==2000
    assert '用户已被注册' in r.json()['msg']



"""
流程性的用例
登录-1.添加商品-2.修改商品-3.查询商品-4.删除商品
"""
import time
from api.goods_func import add_goods,update_goods,query_goods,delete_goods
import pytest


@pytest.mark.smoke
def test_goods_workflow(login_fixture):
    """流程性的用例"""
    #第一步：添加商品
    goodscode = "sp_" + str(int(time.time()))
    r1 =add_goods(login_fixture,"workflow3",goodscode)
    print(r1.text)
    sp_id = r1.json()["data"]["id"]   #获取到新增的商品的id
    assert r1.json()["code"] == 0
    assert r1.json()["msg"] == "success!"
    assert r1.json()["data"]["goodsname"] == "workflow3"

    #第二步：修改商品
    r2 = update_goods(login_fixture,sp_id,"workflow3up",goodscode)
    print(r2.text)
    assert r2.json()["code"] == 0
    assert r2.json()["msg"] == "success!"
    assert r2.json()["data"]["goodsname"] == "workflow3up"

    #第三步：查询商品信息
    r3 = query_goods(login_fixture,sp_id)
    print(r3.text)
    assert r3.json()["code"] == 0
    assert r3.json()["msg"] == "success!"
    assert r3.json()["data"]["goodsname"] == "workflow3up"

    #第四步：删除商品
    r4 = delete_goods(login_fixture,sp_id)
    print(r4.text)
    assert r4.json()["code"] == 0
    assert r4.json()["msg"] == "success!"

    #第五步：再次查询看商品是否已删除
    r5 = query_goods(login_fixture, sp_id)
    print(r5.text)
    assert r5.json()["code"] ==1000
    assert r5.json()["msg"] == "no info"







"""
参数关联用例
案例：添加商品（返回商品id） --> 修改添加的商品
"""
import time
from api.goods_func import add_goods,update_goods


def  test_update_goods(login_fixture):
    """参数关联用例"""
    goodscode = "sp_"+str(int(time.time()))
    r1 = add_goods(login_fixture, "goods_08", goodscode)
    sp_id = r1.json()["data"]["id"]
    print(sp_id)
    r2 = update_goods(login_fixture, sp_id, "goods_08update", goodscode)
    print(r2.text)
    assert r2.json()["code"] ==0
    assert r2.json()["data"]["goodsname"] =="goods_08update"




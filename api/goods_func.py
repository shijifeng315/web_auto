
import requests
from api.login_func import login



def add_goods(s,goodsname,goodscode,**kwargs):
    """添加商品"""
    url = "http://49.235.92.12:7005/api/v2/goods"
    body = {"goodsname":goodsname,
            "goodscode":goodscode
            }
    body.update(kwargs)
    return s.post(url,json=body)

def update_goods(s,sp_id,goodsname,goodscode,**kwargs):
    """更新商品信息"""
    url="http://49.235.92.12:7005/api/v2/goods/{}".format(sp_id)
    body = {"goodsname": goodsname,
            "goodscode": goodscode
            }
    body.update(kwargs)
    return s.put(url,json=body)


def query_goods(s,sp_id):
    """查询商品"""
    url = "http://49.235.92.12:7005/api/v2/goods/{}".format(sp_id)
    return s.get(url)


def delete_goods(s,sp_id):
    """删除商品"""
    url = "http://49.235.92.12:7005/api/v2/goods/{}".format(sp_id)
    return s.delete(url)


if __name__ == '__main__':
    s = requests.Session()
    login(s)
    r1 = add_goods(s,"goods_11","sp_20220114_11")
    sp_id = r1.json()["data"]["id"]
    print(sp_id)
    r2 = update_goods(s,sp_id,"goods_09update","sp_09update")
    print(r1.text)
    print(r2.text)
    r3 = query_goods(sp_id)
    print(r3.text)
    r4 = delete_goods(sp_id)
    print(r4.text)








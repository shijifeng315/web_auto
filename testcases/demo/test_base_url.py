
"""
测试安装的base_url能否使用
"""
import requests

def test_url(base_url):
    print("base_url地址：",base_url)
    r = requests.get(base_url+'/api/test/demo')
    print(r.text)


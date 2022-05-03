import pytest
from api.update_info import update_info
from utils.read_yml import read_yml
from pathlib import Path

p=Path(__file__)  #获取当前文件路径
yamlPath = p.parent.parent.parent.joinpath('data','data.yaml')
test_data =read_yml(yamlPath)['info']

@pytest.mark.parametrize('test_input,expected',test_data)
def test_userinfo(login_fixture,test_input,expected):
    """修改个人信息成功"""
    r = update_info(login_fixture,**test_input)
    print(r.text)
    assert r.json()['code'] == expected['code']
    assert r.json()['message'] == expected['message']

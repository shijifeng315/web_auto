
import pytest
import requests
from api.login_func import login

@pytest.fixture(scope="session")
def login_fixture():
    """可以起到返回session值的作用"""
    s = requests.Session()
    login(s)
    yield s
    #后置清理操作
    s.close()

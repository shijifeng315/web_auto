
from api.login_func import login
import pytest
import requests

@pytest.fixture(scope="session")
def login_fixture():
    s = requests.Session()
    login(s)
    yield s
    #后置清理操作
    s.close()

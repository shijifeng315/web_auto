import requests
from requests import Response

def login(s,username="test1",password="123456") ->Response:
    """
    :param s:
    :param username: 用户名
    :param password: 密码
    :return: session会话
    """
    #先登录拿到token值
    url="http://49.235.92.12:7005/api/v1/login"
    body={
        "username":username,
        "password":password
    }
    r = s.post(url,json=body)
    token=r.json().get("token")
    h={
        "Authorization":"Token {}".format(token)
    }
    s.headers.update(h)
    return r

if __name__ == '__main__':
    s = requests.Session()
    login(s)



from requests import Session,Response
import requests

def update_info(s:Session,
                name="test1",
                sex="F",
                age=20,
                mail="123@qq.com"
                ) ->Response:
    """
    更新个人信息
    :param s: session会话
    :param name:
    :param sex:
    :param age:
    :param mail:
    :return:
    """
    url="http://49.235.92.12:7005/api/v1/userinfo"
    body={
        "name":name,
        "sex":sex,
        "age":age,
        "mail":mail
    }
    r = s.post(url,json=body)
    return r


if __name__ == '__main__':
    from api.login_func import login
    s = requests.Session()
    login(s)
    r = update_info(s)
    print(r.text)

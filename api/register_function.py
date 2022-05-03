
import requests
import time
from requests import Response


def register(username,password='123456') ->Response:
    url="http://49.235.92.12:7005/api/v1/register"
    body={
        "username":username,
        "password":password,
    }
    r=requests.post(url,json=body)
    #print(r.text)
    return r

if __name__ == '__main__':
    r=register("test1xy","123456")
    print(r.text )




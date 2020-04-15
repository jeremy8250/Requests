from pprint import pprint

import requests


def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    pprint(r)

    print(r.status_code)
    print(r.json())
    assert r.status_code == 200


# get请求
def test_get():
    proxies = {
        'http': '127.0.0.1:8888',
        'https': '127.0.0.1:8888'
    }
    r = requests.get("https://httpbin.testing-studio.com/get", params={'a': 1, 'b': 2, 'c': 'cccc'}, proxies=proxies,
                     verify=False)
    print(r.json())
    assert r.status_code == 200


# post请求
def test_form():
    r = requests.post("https://httpbin.testing-studio.com/post", data={'a': 10, 'b': 20, 'c': 'CCCC'})
    print(r.json())
    assert r.status_code == 200


# hook机制
def test_hooks():
    def modify_response(r, *args, **kwargs):
        r.demo = 'demo content'
        return r

    r = requests.post("https://httpbin.testing-studio.com/post", data={'a': 10, 'b': 20, 'c': 'CCCC'},
                      hooks={'response': [modify_response]})
    print(r.json())
    print(r.demo)
    assert r.status_code == 200


# 文件上传
def test_upload():
    files = {'file': open('__init__.py', 'rb')}
    r = requests.post("https://httpbin.testing-studio.com/post", files=files)
    print(r.json())
    assert r.status_code == 200

import json

import requests


class MemberTools:

    def detail(self, token, USERID):
        USER_GET_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = requests.get(USER_GET_URL, params={"access_token": token, "userid": USERID})
        return r.json()

    # 有默认值的参数需要放在没有默认值参数的后面
    def add(self, token, USERID, NAME, MOBILE, DEPTID = "6", **kwargs):
        USER_CREATE_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {"userid": USERID, "name": NAME, "department": DEPTID, "mobile": MOBILE}
        # 后期可以将新的内容传给kwargs并追加到json中参数中
        data.update(kwargs)
        r = requests.post(USER_CREATE_URL, params={"access_token": token}, json=data)
        # 更优雅的打印出json
        print(json.dumps(r.json(), indent=2))
        return r.json()

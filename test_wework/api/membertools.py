import json

import requests

from test_wework.api.wework import WeWork

# 继承WeWork,下面的access_token可以直接调用WeWork中的token，即self.get_token()
class MemberTools(WeWork):
    secret = "OJHobYXhKQjB2FV0cPe1LffCd7J1rqP8xNUBFQ87O68"

    def detail(self, USERID):
        USER_GET_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = requests.get(USER_GET_URL, params={"access_token": self.get_token(self.secret), "userid": USERID})
        return r.json()

    # 有默认值的参数需要放在没有默认值参数的后面
    def add(self, USERID, NAME, MOBILE, DEPTID = "6", **kwargs):
        USER_CREATE_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {"userid": USERID, "name": NAME, "department": DEPTID, "mobile": MOBILE}
        # 后期可以将新的内容传给kwargs并追加到json中参数中
        data.update(kwargs)
        r = requests.post(USER_CREATE_URL, params={"access_token": self.get_token(self.secret)}, json=data)
        # 更优雅的打印出json
        print(json.dumps(r.json(), indent=2))
        return r.json()

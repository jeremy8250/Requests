import requests

from test_wework.api.token import Token


class Department(Token):

    def add(self, name, parentid="1", **kwargs):
        create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {"name": name, "parentid": parentid}
        data.update(kwargs)
        r = requests.post(create_url, params={"access_token": self.get_token(self.corpsecret)}, json=data)
        return r.json()

    def update(self, id, name, **kwargs):
        create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        data = {"id": id, "name": name}
        data.update(kwargs)
        r = requests.post(create_url, params={"access_token": self.get_token(self.corpsecret)}, json=data)
        return r.json()

    def remove(self, id):
        remvoe_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(remvoe_url, params={"access_token": self.get_token(self.corpsecret), "id": id})
        return r.json()

    def query(self, **kwargs):
        query_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params = {"access_token": self.get_token(self.corpsecret)}
        params.update(kwargs)
        r = requests.get(query_url, params=params)
        return r.json()

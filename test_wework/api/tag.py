import requests

from test_wework.api.base_api import BaseApi
from test_wework.api.wework import WeWork


class Tag(WeWork):
    secret = "EZLTFy1FzA7156tchVfT_xW7B6YKDqI5xXQ2TQpWlIg"

    def __init__(self):
        # 将文件加载到self.data中
        self.data = self.api_load("../api/tag.api.yaml")

    def get_api(self):
        # 把tag.api.yaml文件中的get请求读取进来，通过api.send发送请求
        return self.api_send(self.data['get'])


    def get_tag_list(self):
        get_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        data = {"tag_id": []}
        r = requests.post(get_url, params={"access_token": self.get_token(self.secret)}, json=data, )
        self.format(r)
        return r.json()

    def add_tag(self, name, **kwargs):
        add_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        # tag.name字典格式
        data = {"group_id": "ettnklBgAAvsVoVWA4V7LqnOn_IxDFQw", "tag": [{"name": name}]}
        data.update(kwargs)
        r = requests.post(add_url, params={"access_token": self.get_token(self.secret)}, json=data)
        self.format(r)
        return r.json()

    def update_tag(self):
        pass

    def delete_tag(self, tag_id=[], group_id=[]):
        delete_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        data = {"group_id": group_id, "tag_id": tag_id}
        r = requests.post(delete_url, params={"access_token": self.get_token(self.secret)}, json=data)
        self.format(r)
        return r.json()


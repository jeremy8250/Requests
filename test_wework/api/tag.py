import requests

from test_wework.api.base_api import BaseApi
from test_wework.api.wework import WeWork


# 装饰器定义
def api(fun):  # 接收fun函数传参
    def magic(*args, **kwargs):
        base_api: BaseApi = args[0]  # args[0]代表将BaseApi这个类的实例保存到base_api中

        method = fun.__name__  # yaml中的方法名(get/add/delete)=函数名

        base_api.params = kwargs  # 传参
        req = base_api.api_load("../api/tag.api.yaml")[method]  # 加载api.yaml文件,从中找到对应的method
        return base_api.api_send(req)  # 发送请求

    return magic


class Tag(WeWork):
    secret = "EZLTFy1FzA7156tchVfT_xW7B6YKDqI5xXQ2TQpWlIg"

    def __init__(self):
        # 将文件加载到self.data中
        self.data = self.api_load("../api/tag.api.yaml")

    def get_tag_list(self, **kwargs):
        # 把tag.api.yaml文件中的get请求读取进来，通过api.send发送请求
        return self.api_send(self.data['get'])

    # def get_tag_list(self):
    #     get_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
    #     data = {"tag_id": []}
    #     r = requests.post(get_url, params={"access_token": self.get_token(self.secret)}, json=data, )
    #     self.format(r)
    #     return r.json()

    def add_tag(self, name, **kwargs):
        # 将testcase中的name参数值传入parm字典中的中name对应的value
        self.params['name'] = name
        return self.api_send(self.data['add'])

    # def add_tag(self, name, **kwargs):
    #     add_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
    #     # tag.name字典格式
    #     data = {"group_id": "ettnklBgAAvsVoVWA4V7LqnOn_IxDFQw", "tag": [{"name": name}]}
    #     data.update(kwargs)
    #     r = requests.post(add_url, params={"access_token": self.get_token(self.secret)}, json=data)
    #     self.format(r)
    #     return r.json()

    def update_tag(self):
        pass

    def delete_tag(self, tag_id=[], group_id=[]):
        self.params['tag_id'] = tag_id
        self.params['group_id'] = group_id
        return self.api_send(self.data['delete'])

    # def delete_tag(self, tag_id=[], group_id=[]):
    #     delete_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
    #     data = {"group_id": group_id, "tag_id": tag_id}
    #     r = requests.post(delete_url, params={"access_token": self.get_token(self.secret)}, json=data)
    #     self.format(r)
    #     return r.json()

    @api
    def xxx(self, age):
        pass

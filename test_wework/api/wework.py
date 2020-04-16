import datetime
import json

import requests

from test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww73ab17f6d262cc84"
    token = dict()
    token_time = dict()

    # 每个token需要有不同的secret
    @classmethod
    def get_token(cls, secret=None):
        if secret is None:
            # todo: token制度发生变化，在这个地方决定是否重新获取
            return cls.token[secret]
        # 如果secret不在token字典中，则生成token,否则根据secret直接返回一个已经存在的token
        # 避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            # 根据secret传入不同的token到token字典
            cls.token[secret] = r['access_token']
            # cls.token_time[secret] = datetime.now()
        # 从token字段中获取secret key对的token值
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(cls.token_url, params={"corpid": cls.corpid, "corpsecret": secret})
        cls.format(r)
        assert r.json()["errcode"] == 0
        return r.json()



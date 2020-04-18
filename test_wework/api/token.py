import requests
from jsonpath import jsonpath


class Token:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww73ab17f6d262cc84"
    corpsecret = "OJHobYXhKQjB2FV0cPe1LffCd7J1rqP8xNUBFQ87O68"
    token = dict()

    @classmethod
    def get_token(cls, corpsecret=corpsecret):
        if corpsecret is None:
            return cls.token[corpsecret]
        if corpsecret not in cls.token.keys():
            r = cls.get_access_token(corpsecret)
            cls.token[corpsecret] = r['access_token']
        return cls.token[corpsecret]


    @classmethod
    def get_access_token(cls, corpsecret):
        params = {"corpid": cls.corpid, "corpsecret": corpsecret}
        r = requests.get(cls.token_url, params=params)
        assert jsonpath(r.json(), "$..")[0]["errcode"] == 0
        return r.json()

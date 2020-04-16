import requests


class WeWork:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww73ab17f6d262cc84"
    token = dict()

    # 每个token需要有不同的secret
    @classmethod
    def get_token(cls, secret):
        # 如果secret不在token字典中，则生成token,否则根据secret直接返回一个已经存在的token
        # 避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = requests.get(cls.token_url, params={"corpid": cls.corpid, "corpsecret": secret})
            assert r.json()["errcode"] == 0
            # 根据secret传入不同的token到token字典
            cls.token[secret] = r.json()['access_token']
        # 从token字段中获取secret key对的token值
        return cls.token[secret]

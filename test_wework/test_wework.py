import requests
import logging


class TestWeWork:
    logging.basicConfig(level=logging.INFO)
    TOKEN_URL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    ID = "ww73ab17f6d262cc84"
    SECRET = "4-cca7gxN3DzM2W4HWJWjogGbjh6e1PS6lYnUAz-G3c"
    token = None

    # 获取token
    @classmethod
    def setup_class(cls):
        r = requests.get(cls.TOKEN_URL, params={"corpid": cls.ID, "corpsecret": cls.SECRET})
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == "ok"
        cls.token = r.json()['access_token']
        logging.info(cls.token)

    def test_get_token_exist(self):
        assert self.token is not None





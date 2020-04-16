import logging
from test_wework.membertools import MemberTools
from test_wework.wework import WeWork


class TestWeWork:
    logging.basicConfig(level=logging.INFO)
    secret = "OJHobYXhKQjB2FV0cPe1LffCd7J1rqP8xNUBFQ87O68"
    token = None

    # 获取token
    @classmethod
    def setup_class(cls):
        cls.membertools = MemberTools()
        # 传入secrect key，返回对应的token值
        cls.token = WeWork.get_token(cls.secret)

    # 测试token是否正确生成
    def test_get_token_exist(self):
        assert self.token is not None

    # 测试查看用户详情
    def test_get_user_detail(self):
        r = self.membertools.detail(token=self.token, USERID="wangting")
        assert r["errcode"] == 0
        assert r["name"] == "王挺"

    # 测试添加新成员
    def test_add_member(self):
        r = self.membertools.add(token=self.token, USERID="ACCT1241", NAME="testdev1241", MOBILE="13812423838")
        assert r["errcode"] == 0

from test_wework.api.membertools import MemberTools
from test_wework.api.wework import WeWork


class TestWeWork:

    @classmethod
    def setup_class(cls):
        cls.membertools = MemberTools()
        # 传入secrect key，返回对应的token值
        cls.token = WeWork.get_token(cls.membertools.secret)

    # 测试查看用户详情
    def test_get_user_detail(self):
        r = self.membertools.detail(USERID="wangting")
        assert r["errcode"] == 0
        assert r["name"] == "王挺"

    # 测试添加新成员
    def test_add_member(self):
        r = self.membertools.add(USERID="ACCT1241", NAME="testdev1241", MOBILE="13812423838")
        assert r["errcode"] == 0

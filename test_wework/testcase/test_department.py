from jsonpath import jsonpath

from test_wework.api.department import Department
from test_wework.api.token import Token
import random


class TestDepartment:
    num = str(random.randint(1000, 9999))

    @classmethod
    def setup(cls):
        cls.department = Department()
        cls.token = Token.get_token(cls.department.corpsecret)

    def test_create_department(self):
        r = self.department.add(name="testDev_" + self.num)
        assert r["errcode"] == 0

    def test_update_department(self):
        r = self.department.update(id="7", name="testDev_abc")
        assert r["errcode"] == 0

    def test_remove_department(self):
        r = self.department.remove(id="7")
        assert r["errcode"] == 0

    def test_query_department(self):
        r = self.department.query()
        assert r["errcode"] == 0
        print(r)

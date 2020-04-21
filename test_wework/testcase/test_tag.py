import pytest
from jsonpath import jsonpath

from test_wework.api.tag import Tag


class TestTag:
    @classmethod
    def setup(cls):
        cls.tag = Tag()
        # 测试开始前清空测试数据
        cls.reset()

    def test_get_tag_list(self):
        r = self.tag.get_tag_list()
        assert r["errcode"] == 0
        print(self.tag.jsonpath("$..tag[?(@.name!='')]"))

    def test_add_tag(self):
        r = self.tag.add_tag("demo2")
        assert r["errcode"] == 0

    def test_update_tag(self):
        pass

    @pytest.mark.parametrize("name", ["demo1", "中文测试", "中文_1", "123", " ", "*", "👿", ""])
    def test_delete_tag(self, name):
        # 如果有就删除
        r = self.tag.get_tag_list()
        x = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete_tag(tag_id=[x[0]['id']])

        # 环境干净后开始测试
        r = self.tag.get_tag_list()
        path = "$..tag[?(@.name!='')]"
        size = len(self.tag.jsonpath(path))

        # 添加新标签
        self.tag.add_tag(name)
        r = self.tag.get_tag_list()
        assert len(self.tag.jsonpath(path)) == size + 1
        tag_id = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")[0]['id']

        # 删除新标签
        self.tag.delete_tag(tag_id=[tag_id])

        # 断言
        r = self.tag.get_tag_list()
        assert len(self.tag.jsonpath(path)) == size

    def teardown(self):
        # 在你的用例执行被清醒kill的时候，teardown有可能会得不到执行
        self.reset()

    @classmethod
    def reset(cls):
        # grt_tag_list后传入r值
        cls.tag.get_tag_list()
        for name in ['demo1', 'demo2']:
            x = cls.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
            if isinstance(x, list) and len(x) > 0:
                cls.tag.delete_tag(tag_id=[x[0]['id']])

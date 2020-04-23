import pytest
from jsonpath import jsonpath

from test_wework.api.base_api import BaseApi
from test_wework.api.tag import Tag


class TestDDD:
    # 加载yaml文件中的data
    data = BaseApi.yaml_load("test_tag.data.yaml")

    @classmethod
    def setup(cls):
        cls.tag = Tag()
        # 测试开始前清空测试数据
        # cls.reset()

    @pytest.mark.parametrize("name", data["data"])
    def test_delete_tag_by_steps(self, name):
        self.tag.params = {"name": name}
        self.tag.steps_run(self.data['steps'])

    @classmethod
    def reset(cls):
        # grt_tag_list后传入r值
        cls.tag.get_tag_list()
        for name in ['demo1', 'demo2']:
            x = cls.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
            if isinstance(x, list) and len(x) > 0:
                cls.tag.delete_tag(tag_id=[x[0]['id']])

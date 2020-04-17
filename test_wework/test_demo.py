import json

import requests
from jsonpath import jsonpath


class TestDemo:
    def test_jsonpath(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # for item in r.json()["category_list"]["categories"]:
        #     if item["name"] == "开源项目":
        #         break
        # print(item)
        # 使用jsonpath,查找categories下满足name="开源项目"的项，取出第一个数组，取出description字段，判断结果
        assert jsonpath(r.json(), '$..categories[?(@.name=="开源项目")]')[0]['description'] == "开源项目交流与维护"
        # assert item["description"] == "开源项目交流与维护"

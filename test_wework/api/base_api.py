import json

import requests
import yaml
from jsonpath import jsonpath
from requests import Request


class BaseApi:
    # 定义一个params字典，用以存放数据给yaml中的变量
    params = {}
    # 临时存储词典
    data = {}

    @classmethod
    def format(cls, r):
        # 把r缓存到cls.r
        cls.r = r
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None, **kwargs):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)

    # 封装yaml文件的加载
    @classmethod
    # 指定yaml加载后返回一个List类型
    def yaml_load(cls, path) -> list:
        with open(path) as f:
            return yaml.safe_load(f)

    # 将yaml文件读取进来,读取后变成字典格式
    def api_load(self, path):
        return self.yaml_load(path)

    def encode_base64(self):
        pass

    def decode_base64(self, content):
        # todo: 把加密后的内容，解密，并声称一个结构化的数据返回
        return content

    def api_send(self, req: dict):
        # 从wework.get_token方法中获取access_token
        req['params']['access_token'] = self.get_token(self.secret)

        # 将yaml结构化数据转换成字符串
        raw = yaml.dump(req)
        # 将parms字典中的value替换yaml中的带有${key}的值
        for key, value in self.params.items():
            raw = raw.replace(f"${{{key}}}", repr(value))
        # 转成yaml结构化数据
        req = yaml.safe_load(raw)

        # todo: 发送前加密
        # req["xx"] = self.encode_base64()

        # 从req这个字典里面取出key对应的值
        r = requests.request(
            req['method'],
            url=req['url'],
            params=req['params'],
            json=req['json']
        )
        self.format(r)

        # todo: 解密返回的内容
        # return self.decode_base64(r.content)

        return r.json()

    def steps_run(self, steps: list):
        for step in steps:
            # print(step)
            # 将yaml结构化数据转换成字符串
            raw = yaml.dump(step)
            # 将parms字典中的value替换yaml中的带有${key}的值
            for key, value in self.params.items():
                raw = raw.replace(f"${{{key}}}", repr(value))
            # 转成yaml结构化数据
            step = yaml.safe_load(raw)

            if isinstance(step, dict):
                if "method" in step.keys():
                    method = step['method'].split('.')[-1]
                    getattr(self, method)(**step)
                if "extract" in step.keys():
                    self.data[step["extract"]] = getattr(self, 'jsonpath')(**step)
                    # print("extract")
                    # print(self.data[step["extract"]])

                if "assertion" in step.keys():
                    assertion = step["assertion"]
                    # if isinstance(assertion, str):
                    #     assert eval(assertion, str)
                    if assertion[1] == 'eq':
                        assert assertion[0] == assertion[2]

        # # 从wework.get_token方法中获取access_token
        # req['params']['access_token'] = self.get_token(self.secret)
        #
        # # 将yaml结构化数据转换成字符串
        # raw = yaml.dump(req)
        # # 将parms字典中的value替换yaml中的带有${key}的值
        # for key, value in self.params.items():
        #     raw = raw.replace(f"${{{key}}}", repr(value))
        # # 转成yaml结构化数据
        # req = yaml.safe_load(raw)
        #
        # # 从req这个字典里面取出key对应的值
        # r = requests.request(
        #     req['method'],
        #     url=req['url'],
        #     params=req['params'],
        #     json=req['json']
        # )
        # self.format(r)
        # return r.json()

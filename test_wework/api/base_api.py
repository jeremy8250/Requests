import json

import requests
import yaml
from jsonpath import jsonpath
from requests import Request


class BaseApi:
    # 定义一个params字典，用以存放数据给yaml中的变量
    params = {}

    @classmethod
    def format(cls, r):
        # 把r缓存到cls.r
        cls.r = r
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)

    # 封装yaml文件的加载
    @classmethod
    def yaml_load(cls, path) -> list:
        with open(path) as f:
            return yaml.safe_load(f)

    def api_load(self, path):
        # 将yaml文件读取进来,读取后变成字典格式
        return self.yaml_load(path)

    def api_send(self, req: dict):
        # 从WeWork中的get_token方法中获取access_token
        req['params']['access_token'] = self.get_token(self.secret)

        raw = yaml.dump(req)
        for key, value in self.params.items():
            raw = raw.replace(f"${{{key}}}", value)
            print("replace")
        req = yaml.safe_load(raw)

        # 从req这个字典里面取出key对应的值
        r = requests.request(
            req['method'],
            url=req['url'],
            params=req['params'],
            json=req['json']
        )
        self.format(r)
        return r.json()

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # 读取步骤定义文件
            steps: list[dict] = yaml.safe_load(f)
            # 保存一个目标对象
            request: Request = None
            # 找元素找元素，首页需要有元素
            for step in steps:
                # logging.info(step)
                if "by" in step.keys():
                    # 如果在step的key有by
                    element = self.find(step["by"], step["locator"])
                    # 找到by对应的定位方法，找到locator对用的定位符，传给element(这个element类型为WebElement)
                if "action" in step.keys():
                    # 如果在step的key有action
                    action = step["action"]
                    # 取action的值
                    if action == "click":
                        # 如果action为click方法
                        element.click()
                        # 点击元素
                    elif action == "text":
                        # 如果action为text方法
                        element.text
                        # 获取元素的文本
                    elif action == "attribute":
                        # 如果action为attribute方法
                        element.get_attribute(step["value"])
                        # 获取元素的value属性值
                    elif action == "send":
                        # 如果action为send方法
                        content: str = step["value"]
                        # content为send对应的value
                        # 指定content类型为str，才能调用replace()
                        for key in self._params.keys():
                            # 循环遍历所有外部传入的参数
                            content = content.replace("{%s}" % key, self._params[key])
                            # 将外部传入的参数批量替换{}里面的内容
                            # {}为send对应的value值(如value: "{key}")
                        element.send_keys(content)
                        # 发送替换的内容

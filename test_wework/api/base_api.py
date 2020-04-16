import json

import yaml
from requests import Request


class BaseApi:
    @classmethod
    def format(cls, r):
        print(json.dumps(r.json(), indent=2))

    # todo: 封装类似httprunner这样的数据驱动框架
    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # 加了encoding可以防止yaml中文乱码
            steps: list[dict] = yaml.safe_load(f)
            # 读取steps.yaml文件到steps
            # steps为列表中包着词典的类型
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
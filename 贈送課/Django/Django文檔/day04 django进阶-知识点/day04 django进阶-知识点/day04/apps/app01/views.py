import datetime
from django.shortcuts import render


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return "哈哈哈哈哈"


def fetch_data():
    return "我是一个函数"


def gen_data():
    yield 123
    yield 456
    yield 789


def index(request):
    context = {
        "n1": "仙人掌",
        "n2": [11, 22, 33, 44],
        "n3": {
            "name": "武沛齐",
            "age": 19,
        },
        'n4': [
            {"id": 1, "name": "新晨1", "age": 18},
            {"id": 2, "name": "新晨2", "age": 18},
            {"id": 3, "name": "新晨3", "age": 18},
            {"id": 4, "name": "新晨4", "age": 18},
        ],
        "n5": Person("江春", 19),
        "n6": fetch_data,
        "n7": gen_data,
        'n8': "zhangkai",
        "n9": datetime.datetime.now(),
        "n10": datetime.datetime.now().strftime("%Y-%m-%d"),
        "n11": [
            {"id": 1, "name": "xinchen1", "age": 18},
            {"id": 2, "name": "xinchen2", "age": 18},
            {"id": 3, "name": "xinchen3", "age": 18},
            {"id": 4, "name": "xinchen4", "age": 18},
        ],
        "n12": 18
    }
    return render(request, 'app01/index.html', context)


def home(request):
    return render(request, 'app01/home.html', {"title": "路飞学城", "info": "倒闭了"})


def user(request):
    # int("哈哈哈")
    print("函数")
    print(request.resolver_match)  # None
    # return render(request, 'app01/user.html')
    # 事务 + 锁
    from django.template.response import TemplateResponse
    return TemplateResponse(request, 'app01/user.html')

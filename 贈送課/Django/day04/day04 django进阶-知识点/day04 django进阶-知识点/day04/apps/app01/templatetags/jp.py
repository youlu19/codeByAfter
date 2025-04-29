from django import template

register = template.Library()


@register.filter
def myfunc(value):
    return value.upper()


@register.filter
def con(value):
    # ...
    return False


@register.simple_tag
def mytag1():
    return "哈哈哈哈"


@register.simple_tag
def mytag2(a1, a2):
    return a1 + "哈哈哈哈" + a2


@register.inclusion_tag("app01/xxxxx.html")
def xxxxx(arg):
    # <h1>大开哥--73</h1>
    return {"name": "大开哥", "age": 73}


@register.inclusion_tag("app01/menu.html")
def menu(role):

    if role == "user":
        return {
            'data': [
                {"title": "用户管理", "url": "/xxxx/xxx"},
                {"title": "账户管理", "url": "/xxxx/xxx"}
            ]
        }
    if role == 'admin':
        return {
            'data': [
                {"title": "用户管理", "url": "/xxxx/xxx"},
                {"title": "账户管理", "url": "/xxxx/xxx"},
                {"title": "财务", "url": "/xxxx/xxx"},
                {"title": "订单", "url": "/xxxx/xxx"},
            ]
        }

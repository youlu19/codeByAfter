from django.shortcuts import render, HttpResponse

from app01 import models


def index(request):
    # models.UserInfo.objects.create(name='武沛齐', pwd="123123")
    # models.UserInfo.objects.create(name='大军', pwd="123123")

    # models.Blog.objects.create(blog="www.xxx.com", summary='xxxxx', user_id=1)
    # user_object = models.UserInfo.objects.filter(name='大军').first()
    # models.Blog.objects.create(blog="www.xxx.com", summary='xxxxx', user=user_object)

    user_object = models.UserInfo.objects.filter(name='大军').select_related('blog').first()
    print(user_object.name)
    print(user_object.pwd)
    print(user_object.blog.blog)
    print(user_object.blog.summary)

    blog_object = models.Blog.objects.filter(id=1).select_related("user").first()
    print(blog_object.blog)
    print(blog_object.summary)
    print(blog_object.user.name)
    print(blog_object.user.pwd)

    models.UserInfo.objects.filter(name="大军").values("name", 'pwd', 'blog__blog', "blog__summary")

    return HttpResponse("返回")


def login(request):
    # 在session中设置值 + cookie中写入凭证
    request.session['user_info'] = "武沛齐"
    return HttpResponse("登录")


def home(request):
    user_info = request.session.get("user_info")
    print(user_info)
    return HttpResponse("HOME")

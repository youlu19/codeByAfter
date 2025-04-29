from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse


def login(request):
    return render(request, 'api/login.html')


from django.views import View


class UsersView(View):

    def get(self, request):
        # 请求方式GET形式
        return HttpResponse("login")

    def post(self, request):
        # 请求方式POST形式
        return HttpResponse("login")

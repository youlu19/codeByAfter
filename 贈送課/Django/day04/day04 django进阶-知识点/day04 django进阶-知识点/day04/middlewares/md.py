from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMd1(MiddlewareMixin):
    def process_request(self, reqeust):
        print("md1来了")

    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(request, view_func)
        print("view 1")

    def process_response(self, request, response):
        print('md1走了')
        return response

    def process_exception(self, request, exception):
        # 视图函数，抛出异常
        print("异常了", exception)
        return HttpResponse("异常了")

    def process_template_response(self,request,response):
        # 在视图函数中，返回的是TemplateResponse对象；     render方法
        # response.render()
        return response

class MyMd2(MiddlewareMixin):
    def process_request(self, reqeust):
        print("md2来了")

    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(request, view_func)
        print("view 2")

    def process_response(self, request, response):
        print('md2走了')
        return response


class MyMd3(MiddlewareMixin):
    def process_request(self, reqeust):
        print("md3来了")

    def process_response(self, request, response):
        print('md3走了')
        response['xxxxx'] = 123
        return response

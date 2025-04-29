from django.shortcuts import HttpResponse


def auth(request):
    print(request.POST)  # []
    return HttpResponse("auth")

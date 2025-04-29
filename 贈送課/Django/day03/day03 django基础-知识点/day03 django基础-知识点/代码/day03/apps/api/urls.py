from django.urls import path, re_path
from apps.api.views import account

from .views import order

# 很多功能，很多URL
urlpatterns = [
    path('login/', account.login, name="login"),
    path('users/', account.UsersView.as_view(), name='aaaa'),
]

# app_name = "api"

from django.shortcuts import render

# Create your views here.

from django.views import View


class RegisterView(View):
    # 用户注册
    def get(self, request):
        pass

    def post(self, request):
        pass


class Login(View):
    # 用户登陆
    def get(self, request):
        pass

    def post(self, request):
        pass


class CenterView(View):
    # 个人中心
    def get(self, request):
        pass

    def post(self, request):
        pass


class AddressView(View):
    # 收货地址
    def get(self, request):
        pass

    def post(self, request):
        pass


class InfoView(View):
    # 个人资料
    def get(self, request):
        pass

    def post(self, request):
        pass


class LogoutView(View):
    # 退出
    def get(self, request):
        pass

    def post(self, request):
        pass

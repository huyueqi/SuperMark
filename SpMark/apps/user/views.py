from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from django.views import View

from user.forms import AddressForm
from user.models import Address


class RegisterView(View):
    # 用户注册
    def get(self, request):
        return render(request, 'user/reg.html')

    def post(self, request):
        pass


class LoginView(View):
    # 用户登陆
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        pass


class CenterView(View):
    # 个人中心
    def get(self, request):
        return render(request, 'user/member.html')

    def post(self, request):
        pass


class AddressView(View):
    # 收货地址
    def get(self, request):
        return render(request, 'user/address.html')

    def post(self, request):
        #1.接收数据
        val = request.POST
        form = AddressForm(val)
        # 2. 处理数据
        if form.is_valid():
            # 如果接受到了数据
            # 清理数据
            cleaned_data = form.cleaned_data
            Address.objects.create(dorm=cleaned_data.get('dorm'),
                                   tower=cleaned_data.get('tower'),
                                   where=cleaned_data.get('where'),
                                   name=cleaned_data.get('name'),
                                   num=cleaned_data.get('num'),
                                   )
            # 结束显示该页面
            return render(request, 'user/address.html')
        # else:
        #     # 如果没有,跳转到当前继续添加
        #     return redirect(reverse('user:address'))


class InfoView(View):
    # 个人资料
    def get(self, request):
        return render(request, 'user/infor.html')

    def post(self, request):
        pass


class LogoutView(View):
    # 退出
    def get(self, request):
        pass

    def post(self, request):
        pass

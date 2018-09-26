from django import forms
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from django.views import View

# from user.forms import AddressForm
# from user.models import Address
from user.forms import RegisterForm, LoginForm
from user.models import User


class RegisterView(View):
    # 用户注册
    def get(self, request):
        # 渲染
        form = RegisterForm()
        val = {
            'form': form
        }
        return render(request, 'user/reg.html', val)

    def post(self, request):
        # 1.接收数据
        # 2.回复数据
        form = RegisterForm(request.POST)
        # 3.处理数据
        if form.is_valid():
            form.save()
            # 注册成功,跳转到登陆页面
            return redirect(reverse('user:login'))
        # 注册失败,跳转到注册页面,并提示错误信息
        return render(request, 'user/reg.html', {'form': form})


class LoginView(View):
    # 用户登陆
    def get(self, request):
        # 用来渲染
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        # 1.接收数据
        # 2.回复数据
        form = LoginForm(request.POST)
        # 3.处理数据
        if form.is_valid():
            # form.save()
            # 保存个人标识
            user = form.cleaned_data.get('user')
            request.session['id'] = user.id
            request.session['phone'] = user.phone
            # 登陆成功,跳转到个人中心
            return redirect(reverse('user:center'))
        # 失败,继续登陆,返回错误信息
        return render(request, 'user/login.html', {'form': form})


class CenterView(View):
    # 个人中心
    def get(self, request):
        phone = request.session.get('phone')
        return render(request, 'user/member.html', {'phone': phone})

    def post(self, request):
        pass


class AddressView(View):
    # 收货地址
    def get(self, request):
        return render(request, 'user/address.html')

    def post(self, request):
        # 1.接收数据
        # val = request.POST
        # form = AddressForm(val)
        # 2. 处理数据
        # if form.is_valid():
        # 如果接受到了数据
        # 清理数据
        # cleaned_data = form.cleaned_data
        # User.objects.create(dorm=cleaned_data.get('dorm'),
        #                        tower=cleaned_data.get('tower'),
        #                        where=cleaned_data.get('where'),
        #                        name=cleaned_data.get('name'),
        #                        num=cleaned_data.get('num'),
        #                        )
        # 结束显示该页面
        # return render(request, 'user/address.html')
        # else:
        #     # 如果没有,跳转到当前继续添加
        #     return redirect(reverse('user:address'))
        pass


class InfoView(View):
    # 个人资料
    def get(self, request):
        return render(request, 'user/infor.html')

    def post(self, request):
        val = request.POST
        pass


def upload_head(request):
    if request.method == 'POST':
        # 获取用户的id
        user_id = request.session.get("ID")
        # 获取用户的对象
        user = User.objects.get(pk=user_id)
        # 保存图片
        user.head = request.FILES['file']
        user.save()
        return JsonResponse({'error': 0})
    else:
        return JsonResponse({'error': 1})


class LogoutView(View):
    # 退出
    def get(self, request):
        auth.logout(request)
        return redirect(reverse('user:login'))

    def post(self, request):
        pass

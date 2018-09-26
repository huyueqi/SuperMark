# from django import forms
#
#
# class AddressForm(forms.Form):
#     dorm = forms.CharField()
from django import forms
from django.shortcuts import redirect
from django.urls import reverse

from user.helper import new_password
from user.models import User


class RegisterForm(forms.ModelForm):
    # 确认密码
    repassword = forms.CharField(max_length=16,
                                 min_length=8,
                                 error_messages={
                                     'required': '请填写确认密码',
                                 },
                                 widget=forms.PasswordInput(
                                     attrs={'class': 'login-password', 'placeholder': '请输入确认密码'}),
                                 )

    # 注册的表单
    class Meta:
        model = User
        fields = ['phone', 'password']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'login-name', 'placeholder': '请输入手机号'}),
            'password': forms.PasswordInput(attrs={'class': 'login-password', 'placeholder': '请输入您的密码'}),
        }
        # 错误信息
        error_messages = {
            'phone': {
                'required': '请填写电话号码正确格式'
            },
            'password': {
                'required': '请输入密码'
            },

        }

    # 'repassword': {
    #     'required': '请输入登陆密码'
    # },
    def clean_phone(self):
        # 获取清洗后的数据
        new_phone = self.cleaned_data.get('phone')
        # 数据库来查询数据
        val = User.objects.filter(phone=new_phone).exists()
        # 比较数据
        if val:
            # 如果是一样的,就报错误
            raise forms.ValidationError('号码已存在')
        return new_phone

    # 验证登陆密码和确认密码是否一致
    def clean(self):
        # 获取数据
        cleaned_data = super().clean()
        var1 = cleaned_data.get('password')
        var2 = cleaned_data.get('repassword')
        # 开始比较两个值是否一致
        if var1 and var2 and var1 != var2:
            raise forms.ValidationError({'repassword': '密码不一致'})
        else:
            cleaned_data['password'] = new_password(var1)
        return cleaned_data


class LoginForm(forms.ModelForm):
    # 登陆的表单
    class Meta:
        model = User
        fields = ['phone', 'password']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'login-name', 'placeholder': '请输入用户名/手机号'}),
            'password': forms.PasswordInput(attrs={'class': 'login-password', 'placeholder': '请输入密码'}),
        }

        error_messages = {
            'phone': {
                'required': '请输入电话号码'
            },
            'password': {
                'required': '请输入密码'
            },
        }

    def clean(self):
        # 获取清理后的数据
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        password = cleaned_data.get('password')
        # 取出数据库中的数据
        user = User.objects.filter(phone=phone).first()
        # 比较
        if user is None:
            # 如果值没有,就发送错误
            raise forms.ValidationError({'phone': '手机号码不正确'})
        else:
            # 有电话,验证密码是否正确
            password_db = user.password
            password = new_password(password)
            # 吧用户输入密码和数据库提取密码比较
            if password == password_db:
                # 保存一个清洗后的user对象
                cleaned_data['user'] = user
                return cleaned_data
            else:
                raise forms.ValidationError({'password': '密码错误'})

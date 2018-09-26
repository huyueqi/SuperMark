# Create your models here.
# class Address(models.Model):
#     dorm = models.CharField(max_length=20)  # 宿舍区
#     tower = models.CharField(max_length=20)  # 哪栋楼
#     where = models.CharField(max_length=20)  # 你在哪
#     name = models.CharField(max_length=20)  # 收货人
#     num = models.SmallIntegerField(13)  # 电话号码
#
#
# class Register(models.Model):
#     phone = models.CharField(max_length=11) # 手机号码
#     password = models.CharField(max_length=16)  # 登陆密码
from django.core import validators
from django.db import models


class User(models.Model):
    sex_choice = (
        (0, '男'),
        (1, '女'),
        (3, '保密')
    )
    name = models.CharField(max_length=20, verbose_name='昵称', null=True, blank=True)
    sex = models.SmallIntegerField(choices=sex_choice, default=1, verbose_name='性别')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    school = models.CharField(max_length=20, verbose_name='学校', null=True, blank=True)
    place = models.CharField(max_length=20, verbose_name='位置', null=True, blank=True)
    hometown = models.CharField(max_length=20, verbose_name='故乡', null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='电话',
                             validators=[validators.RegexValidator(r'^1[3-9]\d{9}$', '手机格式化错误!')])
    password = models.CharField(max_length=64, verbose_name='密码')


    def __str__(self):
        return self.phone



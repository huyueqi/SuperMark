from django.db import models


# Create your models here.
class Address(models.Model):
    dorm = models.CharField(max_length=20)  # 宿舍区
    tower = models.CharField(max_length=20)  # 哪栋楼
    where = models.CharField(max_length=20)  # 你在哪
    name = models.CharField(max_length=20)  # 收货人
    num = models.SmallIntegerField(13)  # 电话号码



from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from db.base import BaseModel

added_choices = (
    (0, '上架'),
    (1, '下架'),
)


# Create your models here.
# 商品分类表
class Sort(models.Model):
    name = models.CharField(max_length=30, verbose_name='商品分类的名字')
    intro = models.TextField(max_length=100, verbose_name='商品分类的简介', null=True, blank=True)
    is_delete = models.BooleanField(verbose_name="是否删除", default=False, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = verbose_name


# 商品SPU表
class SPU(models.Model):
    name = models.CharField(max_length=30, verbose_name='商品SPU表的名字')
    detail = RichTextUploadingField(verbose_name="商品详情")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品SPU"
        verbose_name_plural = verbose_name


# 商品单位表
class Unit(models.Model):
    name = models.CharField(max_length=20, verbose_name='商品的单位')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品单位"
        verbose_name_plural = verbose_name


# 商品SKU表
class SKU(models.Model):
    sku_name = models.CharField(max_length=100, verbose_name='商品SKU名称', )
    brief = models.CharField(max_length=200, verbose_name="商品的简介", null=True, blank=True, )
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='价格', )
    unit = models.ForeignKey(to="Unit", verbose_name='单位', )
    stock = models.IntegerField(default=100, verbose_name='库存', )
    sale_num = models.IntegerField(default=0, verbose_name='销量', )
    logo = models.ImageField(upload_to='static/%Y%m/%d', verbose_name='封面图片', )
    added = models.BooleanField(choices=added_choices, verbose_name="是否上架", default=0)
    sort = models.ForeignKey(to="Sort", verbose_name='商品分类', )
    spu = models.ForeignKey(to="SPU", verbose_name="商品SPU", )
    is_delete = models.BooleanField(verbose_name="是否删除", default=False, )

    def __str__(self):
        return self.sku_name

    class Meta:
        verbose_name = "商品SKU"
        verbose_name_plural = verbose_name


# 商品相册表
class Images(models.Model):
    site = models.ImageField(upload_to='static/%Y%m/%d', verbose_name='图片地址')
    sku = models.ForeignKey(to='SKU', verbose_name='商品SKU')

    class Meta:
        verbose_name = "商品相册"
        verbose_name_plural = verbose_name


# 首页轮播
class Banner(BaseModel):
    name = models.CharField(max_length=100, verbose_name='轮播活动名字')
    cargo_sku = models.ForeignKey(to='SKU', verbose_name='商品SKU表')
    img = models.ImageField(upload_to='static/%Y%m/%d', verbose_name='轮播图片地址')
    order = models.SmallIntegerField(verbose_name='排序', default=0)

    class Meta:
        verbose_name = "首页轮播"
        verbose_name_plural = verbose_name


# 首页活动
class Event(BaseModel):
    title = models.CharField(max_length=150, verbose_name='活动名称', )
    img = models.ImageField(verbose_name='活动图片地址', upload_to='static/%Y%m/%d')
    url_site = models.CharField(verbose_name='活动的url地址', max_length=200)

    def __str__(self):
        return self.title


# 首页活动专区
class ActivityZone(BaseModel):
    title = models.CharField(verbose_name='活动专区名称', max_length=150)
    brief = models.CharField(verbose_name="活动专区的简介", max_length=200, null=True, blank=True, )
    order = models.SmallIntegerField(verbose_name="排序", default=0, )
    added = models.BooleanField(verbose_name="上否上线", choices=added_choices, default=0, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "活动管理"
        verbose_name_plural = verbose_name


# 首页活动专区商品列表
class ActivityZoneGoods(BaseModel):
    activity_zone = models.ForeignKey(to="ActivityZone", verbose_name="活动专区ID", )
    goods_sku = models.ForeignKey(to="SKU", verbose_name="专区商品SKU_ID", )

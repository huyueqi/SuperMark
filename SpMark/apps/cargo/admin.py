from django.contrib import admin

# Register your models here.
from cargo.models import Sort, SPU, Unit, SKU, Images, ActivityZoneGoods, ActivityZone, Event, Banner

admin.site.site_header = "超级电商管理平台"

# 商品分类
@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    pass


# 商品SUP表
@admin.register(SPU)
class SPUAdmin(admin.ModelAdmin):
    pass


# 商品单位表
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


# 商品SKU
@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):
    pass


# 商品相册表


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass


# 首页轮播

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


# 首页活动
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


# # 首页活动专区
# @admin.register(ActivityZone)
# class ActivityZoneAdmin(admin.ModelAdmin):
#     inlines = [
#         ActivityZoneAdminInline
#     ]
#
#
# # 首页活动专区商品列表
# @admin.register(ActivityZoneGoods)
# class ActivityZoneGoodsAdmin(admin.StackedInline):
#     model = ActivityZoneAdmin
#     extra = 2

# 注册ActivityZone的模型到后台
class ActivityZoneAdminInline(admin.StackedInline):
    model = ActivityZoneGoods
    extra = 2


@admin.register(ActivityZone)
class ActivityZoneAdmin(admin.ModelAdmin):
    inlines = [
        ActivityZoneAdminInline
    ]
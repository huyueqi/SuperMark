from django.conf.urls import url

from cargo.views import IndexView, CategoryView, DetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 首页
    url(r'^category/(?P<cate_id>\d+)/(?P<order>\d+)$', CategoryView.as_view(), name='category'),  # 货物分类
    url(r'^detail/(?P<sku_id>\d+)$', DetailView.as_view(), name='detail'),  # 货物详情
]
# (?P<dex_id>\d+)
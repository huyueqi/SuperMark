from django.shortcuts import render

# Create your views here.
from django.views import View

from cargo.models import SKU, Sort, Banner


class IndexView(View):
    # 商城首页
    def get(self, request):
        # 接收
        # dex_id = int(dex_id)
        ban = Banner.objects.all()
        # 处理
        # 获取所有产品遍历到特色专区下面
        sku = SKU.objects.filter(is_delete=False)
        # 响应
        val = {
            'ban': ban,
            'sku': sku,
        }
        return render(request, 'cargo/index.html', val)

    def post(self, request):
        pass


class CategoryView(View):
    # 超市货物的分类
    def get(self, request, cate_id, order):
        """
        排序: 设置一个参数: order = 0,1,2,3 ===> 综合,销量,价格
        排序: 模型对象.objects.all().order_by(-"字段")
        映射关系: ['id','-sale_num','price','-price']
        """
        # 通过条件查询所有的列表
        # sort = Sort.objects.filter(is_delete=False)
        cate_id = int(cate_id)
        order = int(order)
        # 查询出所有分类进行显示
        sorts = Sort.objects.filter(is_delete=False)
        if cate_id == 0:
            # 默认展示第一个分类下的商品
            sort = sorts.first()
            # 如果ID=0,ID就应该为分类的pk
            cate_id = sort.pk
        else:
            # 获取传入分类ID对应的分类
            sort = Sort.objects.get(pk=cate_id)
        # 设置映射关系
        order_by = ['id', '-sale_num', 'price', '-price']
        # 对应分类下的商品
        sku = sort.sku_set.all().order_by(order_by[order])
        # sku = SKU.objects.filter(is_delete=False, cate_id=cate_id)
        val = {
            'sorts': sorts,
            'sku': sku,
            'cate_id': cate_id,
            'order': order,
        }
        return render(request, 'cargo/category.html', val)

    def post(self, request):
        pass


class DetailView(View):
    # 超市货物的详情
    def get(self, request, sku_id):
        # 接收
        sku_id = int(sku_id)
        # 处理
        cargo_sku = SKU.objects.get(pk=sku_id)
        # 响应
        # cargo_sku.images_set.all()
        return render(request, 'cargo/detail.html', {'cargo_sku': cargo_sku})

    def post(self, request):
        pass

#

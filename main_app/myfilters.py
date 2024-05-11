import django_filters
from api_app.models import Goods, Brands, Category, Colors, Sizes, HugeCard, MainCats, MainBrands, MainProducts, \
    SizesToGoodTable, Order, GoodToUser


class GoodsFilter(django_filters.FilterSet):
    class Meta:
        model = Goods
        fields = {
            'model_name': ['icontains'],
            'price': ['lt', 'gt'],
            'category': ['exact'],
            'brand_id': ['exact'],
            'sale_confirmed': ['exact'],
            # 'articul': ['icontains'],
            'is_active': ['exact']
        }


class BrandFilter(django_filters.FilterSet):
    brand_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Brands
        fields = {
            'brand_name': ['icontains'],
            'is_active': ['exact']
        }


class CatsFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['icontains'],
            'is_active': ['exact'],
            'brand': ['exact'],
        }


class ColorsFilter(django_filters.FilterSet):
    class Meta:
        model = Colors
        fields = {
            'color': ['icontains'],
            'is_active': ['exact'],
        }


class SizesFilter(django_filters.FilterSet):
    class Meta:
        model = Sizes
        fields = {
            'size': ['icontains'],
            'is_active': ['exact'],
        }


class HugeCardFilter(django_filters.FilterSet):
    class Meta:
        model = HugeCard
        fields = {
            'description': ['icontains'],
            'is_active': ['exact'],
            'good_id': ['exact']
        }


class MainCatsFilter(django_filters.FilterSet):
    class Meta:
        model = MainCats
        fields = {
            'is_active': ['exact'],
            'cat_id': ['exact']
        }


class MainBrandsFilter(django_filters.FilterSet):
    class Meta:
        model = MainBrands
        fields = {
            'is_active': ['exact'],
            'brand_id': ['exact']
        }


class MainProductsFilter(django_filters.FilterSet):
    class Meta:
        model = MainProducts
        fields = {
            'is_active': ['exact'],
            'good_id': ['exact'],
        }


class SizeToGoodTableFilter(django_filters.FilterSet):
    class Meta:
        model = SizesToGoodTable
        fields = {
            'is_active': ['exact'],
            'good': ['exact'],
            'size': ['exact'],
            'count': ['lt', 'gt']
        }


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'is_active': ['exact'],
            'user': ['exact'],
            'phone_number': ['icontains']
        }


class OrderToGoodFilter(django_filters.FilterSet):
    class Meta:
        model = GoodToUser
        fields = {
            'is_active': ['exact'],
            'order': ['exact'],
            'good': ['exact']
        }





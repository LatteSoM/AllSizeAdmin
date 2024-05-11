from rest_framework import serializers
from .models import Users, Brands, Category, Colors, Sizes, Goods, HugeCard, MainCats, MainBrands, MainProducts, SizesToGoodTable, Order, GoodToUser


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Users
        fields = ['id', 'login', 'password', 'role_id']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.brand_name = validated_data.get('brand_name', instance.brand_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = '__all__'


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class HugeCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HugeCard
        fields = '__all__'



class MainCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCats
        fields = '__all__'


class MainBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBrands
        fields = '__all__'


class MainProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProducts
        fields = '__all__'


class SizesToGoodTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizesToGoodTable
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class GoodToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodToUser
        fields = '__all__'




from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import ManyToManyField

from .manager import UserManager


# Create your models here.

class Roles(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Users(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=260)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["password"]
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Brands(models.Model):
    brand_name = models.CharField(max_length=50)
    brands_pic = models.ImageField(null=True, upload_to='image')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.brand_name


class Category(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    cat_pic = models.ImageField(null=True, upload_to='image')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class Colors(models.Model):
    color = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.color


class Sizes(models.Model):
    size = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.size


class Goods(models.Model):
    model_name = models.CharField(max_length=250)
    main_pic = models.ImageField(null=True, upload_to='image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brands, max_length=250, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    # price = models.DecimalField(max_digits=6, decimal_places=0)
    price = models.IntegerField()
    price_with_sale = models.IntegerField(blank=True)
    color_id = models.ForeignKey(Colors, on_delete=models.CASCADE)
    articul = models.CharField(max_length=50, blank=True)
    sale_confirmed = models.BooleanField()
    size = models.ManyToManyField(Sizes, through='SizesToGoodTable')
    is_active = models.BooleanField(default=True)
    # price_formatted = intcomma(price)

    def __str__(self):
        return self.model_name

    @property
    def price_formatted(self):
        return '{:,.0f}'.format(self.price).replace(',', ' ')

    @property
    def price_with_sale_formatted(self):
        return '{:,.0f}'.format(self.price_with_sale).replace(',', ' ')


class HugeCard(models.Model):
    good_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    description = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)


class MainCats(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class MainBrands(models.Model):
    brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class MainProducts(models.Model):
    good_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class SizesToGoodTable(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)


class Order(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods, through='GoodToUser')
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)


class GoodToUser(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)









# from django.db import models
#
# # Create your models here.
#
# from django.db import models
# from django.contrib.humanize.templatetags.humanize import intcomma
# # import
#
# # Create your models here.
#
#
# class Brands(models.Model):
#     brand_name = models.CharField(max_length=50)
#     brands_pic = models.ImageField(null=True, upload_to='image')
#
#     def __str__(self):
#         return self.brand_name
#
#
# class Category(models.Model):
#     brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
#     category_name = models.CharField(max_length=50)
#     cat_pic = models.ImageField(null=True, upload_to='image')
#
#     def __str__(self):
#         return self.category_name
#
#
# class Colors(models.Model):
#     color = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.color
#
#
# class Sizes(models.Model):
#     size = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.size
#
#
# class Goods(models.Model):
#     model_name = models.CharField(max_length=250)
#     main_pic = models.ImageField(null=True, upload_to='image')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     brand_id = models.ForeignKey(Brands, max_length=250, on_delete=models.CASCADE)
#     description = models.CharField(max_length=250)
#     # price = models.DecimalField(max_digits=6, decimal_places=0)
#     price = models.IntegerField()
#     price_with_sale = models.IntegerField(blank=True)
#     color_id = models.ForeignKey(Colors, on_delete=models.CASCADE)
#     articul = models.CharField(max_length=50, blank=True)
#     sale_confirmed = models.BooleanField()
#     size = models.ManyToManyField(Sizes, through='SizesToGoodTable')
#     # price_formatted = intcomma(price)
#
#     def __str__(self):
#         return self.model_name
#
#     @property
#     def price_formatted(self):
#         return '{:,.0f}'.format(self.price).replace(',', ' ')
#
#     @property
#     def price_with_sale_formatted(self):
#         return '{:,.0f}'.format(self.price_with_sale).replace(',', ' ')
#
#
# class HugeCard(models.Model):
#     good_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
#     description = models.CharField(max_length=60)
#
#
# class MainCats(models.Model):
#     cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#
# class MainBrands(models.Model):
#     brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE)
#
#
# class MainProducts(models.Model):
#     good_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
#
#
# class SizesToGoodTable(models.Model):
#     good = models.ForeignKey(Goods, on_delete=models.CASCADE)
#     size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
#     count = models.IntegerField()
#
#
# # class Images(models.Model):
# #     imga = models.ImageField(upload_to='image')
# #     good_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
#
#

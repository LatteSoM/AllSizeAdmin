# from django.contrib import admin
# from django.urls import path, include
# import api_app.views as v
# # from .views import RegistrationAPIView, LoginAPIView
#
#
# urlpatterns = [
#     path('register/<str:login>/<str:password>/<int:role>/', v.UserRegistrationAPIView.as_view, name='register'),
#     path('login/<str:login>/<str:password>/', v.UserLoginAPIView.as_view, name='login'),
# ]
# from xml.etree.ElementInclude import include

from django.urls import re_path, path, include
from rest_framework.routers import DefaultRouter

from api_app import views
# from api_app.views import BrandViewSet, CategoryViewSet, ColorsViewSet, GoodToUserViewSet, SizesViewSet, GoodsViewSet, \
#     HugeCardViewSet, MainCatsViewSet, MainBrandsViewSet, MainProductsViewSet, SizesToGoodTableViewSet, OrderViewSet

# router = DefaultRouter()
# router.register(r'brands', BrandViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'colors', ColorsViewSet)
# router.register(r'sizes', SizesViewSet)
# router.register(r'goods', GoodsViewSet)
# router.register(r'hugecard', HugeCardViewSet)
# router.register(r'maincats', MainCatsViewSet)
# router.register(r'mainbrands', MainBrandsViewSet)
# router.register(r'mainproducts', MainProductsViewSet)
# router.register(r'sizetogoodtable', SizesToGoodTableViewSet)
# router.register(r'order', OrderViewSet)
# router.register(r'goodtouser', GoodToUserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    path('brands/', views.BrandAPIList.as_view()),
    path('brands/<int:pk>', views.BrandAPIListAptDel.as_view()),
    # path('search/')
]

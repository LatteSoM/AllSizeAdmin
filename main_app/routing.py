from django.urls import path
import main_app.views as v
from Pract import settings
from django.conf.urls.static import static as djstat

# from main_app import views


urlpatterns = [
    path('', v.register, name='index'),
    path('login/', v.user_login, name='login_page'),
    path('home/', v.home_page, name='home'),

    path('goods/', v.GoodsListView.as_view(), name='goods_list'),
    path('goods/<int:pk>/', v.GoodsDetailView.as_view(), name='goods_detail'),
    path('goods/add/', v.GoodsCreateView.as_view(), name='goods_add'),
    path('goods/<int:pk>/update/', v.GoodsUpdateView.as_view(), name='goods_update'),
    path('goods/<int:pk>/delete/', v.GoodsDeleteView.as_view(), name='goods_delete'),

    path('brands/', v.BrandsListView.as_view(), name='brands_list'),
    path('brands/<int:pk>/', v.BrandsDetailView.as_view(), name='brands_detail'),
    path('brands/add/', v.BrandsCreateView.as_view(), name='brands_add'),
    path('brands/<int:pk>/update/', v.BrandsUpdateView.as_view(), name='brands_update'),
    path('brands/<int:pk>/delete/', v.BrandsDeleteView.as_view(), name='brands_delete'),

    path('cats/', v.CategoryListView.as_view(), name='cats_list'),
    path('cats/<int:pk>/', v.CategoryDetailView.as_view(), name='cats_detail'),
    path('cats/add/', v.CategoryCreateView.as_view(), name='cats_add'),
    path('cats/<int:pk>/update/', v.CategoryUpdateView.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', v.CategoryDeleteView.as_view(), name='cats_delete'),

    path('colors/', v.ColorsListView.as_view(), name='colors_list'),
    path('colors/<int:pk>/', v.ColorsDetailView.as_view(), name='colors_detail'),
    path('colors/add/', v.ColorsCreateView.as_view(), name='colors_add'),
    path('colors/<int:pk>/update/', v.ColorsUpdateView.as_view(), name='colors_update'),
    path('colors/<int:pk>/delete/', v.ColorsDeleteView.as_view(), name='colors_delete'),

    path('sizes/', v.SizesListView.as_view(), name='sizes_list'),
    path('sizes/<int:pk>/', v.SizesDetailView.as_view(), name='sizes_detail'),
    path('sizes/add/', v.SizesCreateView.as_view(), name='sizes_add'),
    path('sizes/<int:pk>/update/', v.SizesUpdateView.as_view(), name='sizes_update'),
    path('sizes/<int:pk>/delete/', v.SizesDeleteView.as_view(), name='sizes_delete'),

    path('hugecards/', v.HugeCardListView.as_view(), name='hugecards_list'),
    path('hugecards/<int:pk>/', v.HugeCardDetailView.as_view(), name='hugecards_detail'),
    path('hugecards/add/', v.HugeCardCreateView.as_view(), name='hugecards_add'),
    path('hugecards/<int:pk>/update/', v.HugeCardUpdateView.as_view(), name='hugecards_update'),
    path('hugecards/<int:pk>/delete/', v.HugeCardDeleteView.as_view(), name='hugecards_delete'),

    path('maincats/', v.MainCatsListView.as_view(), name='maincats_list'),
    path('maincats/<int:pk>/', v.MainCatsDetailView.as_view(), name='maincats_detail'),
    path('maincats/add/', v.MainCatsCreateView.as_view(), name='maincats_add'),
    path('maincats/<int:pk>/update/', v.MainCatsUpdateView.as_view(), name='maincats_update'),
    path('maincats/<int:pk>/delete/', v.MainCatsDeleteView.as_view(), name='maincats_delete'),

    path('mainbrands/', v.MainBrandsListView.as_view(), name='mainbrands_list'),
    path('mainbrands/<int:pk>/', v.MainBrandsDetailView.as_view(), name='mainbrands_detail'),
    path('mainbrands/add/', v.MainBrandsCreateView.as_view(), name='mainbrands_add'),
    path('mainbrands/<int:pk>/update/', v.MainBrandsUpdateView.as_view(), name='mainbrands_update'),
    path('mainbrands/<int:pk>/delete/', v.MainBrandsDeleteView.as_view(), name='mainbrands_delete'),

    path('mainproducts/', v.MainProductsListView.as_view(), name='mainproducts_list'),
    path('mainproducts/<int:pk>/', v.MainProductsDetailView.as_view(), name='mainproducts_detail'),
    path('mainproducts/add/', v.MainProductsCreateView.as_view(), name='mainproducts_add'),
    path('mainproducts/<int:pk>/update/', v.MainProductsUpdateView.as_view(), name='mainproducts_update'),
    path('mainproducts/<int:pk>/delete/', v.MainProductsDeleteView.as_view(), name='mainproducts_delete'),

    path('sizestogoodtable/', v.SizeToGoodTableListView.as_view(), name='sizestogoodtable_list'),
    path('sizestogoodtable/<int:pk>/', v.SizeToGoodTableDetailView.as_view(), name='sizestogoodtable_detail'),
    path('sizestogoodtable/add/', v.SizeToGoodTableCreateView.as_view(), name='sizestogoodtable_add'),
    path('sizestogoodtable/<int:pk>/update/', v.SizeToGoodTableUpdateView.as_view(), name='sizestogoodtable_update'),
    path('sizestogoodtable/<int:pk>/delete/', v.SizeToGoodTableDeleteView.as_view(), name='sizestogoodtable_delete'),

    path('order/', v.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', v.OrderDetailView.as_view(), name='order_detail'),
    path('order/add/', v.OrderCreateView.as_view(), name='order_add'),
    path('order/<int:pk>/update/', v.OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', v.OrderDeleteView.as_view(), name='order_delete'),

    path('ordertouser/', v.GoodToListView.as_view(), name='ordertouser_list'),
    path('ordertouser/<int:pk>/', v.GoodToDetailView.as_view(), name='ordertouser_detail'),
    path('ordertouser/add/', v.GoodToCreateView.as_view(), name='ordertouser_add'),
    path('ordertouser/<int:pk>/update/', v.GoodToUpdateView.as_view(), name='ordertouser_update'),
    path('ordertouser/<int:pk>/delete/', v.GoodToDeleteView.as_view(), name='ordertouser_delete'),
] + djstat(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

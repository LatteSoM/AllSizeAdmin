# # from django.contrib.auth import authenticate
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status, viewsets
# # from api_app.models import Users
# # from rest_framework.authtoken.models import Token
# # from rest_framework.authentication import TokenAuthentication
# # from rest_framework.permissions import AllowAny
# #
# #
# # class UserRegistrationAPIView(viewsets.ModelViewSet):
# #     authentication_classes = ()
# #     permission_classes = (AllowAny,)
# #
# #     def post(self, request, login, password, role):
# #         print('dfghjkl;')
# #
# #         if login is None or password is None:
# #             return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
# #
# #         if Users.objects.filter(login=login).exists():
# #             return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
# #
# #         user = Users.objects.create(login=login, password=password, role_id=role)
# #         token, created = Token.objects.get_or_create(user=user)
# #         print(user, 'dfghjkl;')
# #         return Response({'token': token.key}, status=status.HTTP_201_CREATED)
# #
# #
# # class UserLoginAPIView(viewsets.ModelViewSet):
# #     authentication_classes = ()
# #     permission_classes = (AllowAny,)
# #
# #     def post(self, request, login, password):
# #
# #         user = authenticate(login=login, password=password)
# #
# #         if not user:
# #             return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
# #
# #         token, created = Token.objects.get_or_create(user=user)
# #         return Response({'token': token.key}, status=status.HTTP_200_OK)

from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.views import FilterView
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from main_app.myfilters import *
#
# from main_app.myfilters import BrandFilter
from .models import *
from .permissions import IsAdminUser
from .serializers import *


from rest_framework.authtoken.models import Token

from api_app.serializers import UserSerializer, BrandSerializer, CategorySerializer, ColorsSerializer, SizesSerializer, \
    GoodsSerializer, HugeCardSerializer, MainCatsSerializer, MainBrandsSerializer, MainProductsSerializer, \
    SizesToGoodTableSerializer, OrderSerializer, GoodToUserSerializer
from .permissions import IsAdminUser, IsDefaultUser

#
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = Users.objects.get(login=request.data['login'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    # return Response(serializer.errors, status=status.HTTP_200_OK)
    # return Response({})


@api_view(['POST'])
def login(request):
    user = get_object_or_404(Users, login=request.data['login'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")
#
#
# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brands.objects.all()
#     serializer_class = BrandSerializer
#     # filterset_class = BrandFilter
#     # filter_queryset = Brands.objects.all().order_by('brand_name')
#     # filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
#     # filterset_fields = ['is_active']  # Поля, по которым можно фильтровать
#     # search_fields = ['brand_name']  # Поля, по которым можно искать
#     # ordering_fields = ['brand_name', 'is_active']  # Поля, по которым можно сортировать
#     permission_classes = [IsAuthenticated]
#
#     #@action(methods=['GET'], detail=False)
#     def put(self, request, pk):
#         temp_instance = Brands.objects.get(pk=pk)
#         serializer_for_upd = self.serializer_class(temp_instance, data=request.data)
#         serializer_for_upd.is_valid(raise_exception=True)
#         serializer_for_upd.update(temp_instance, serializer_for_upd.validated_data)
#         return Response(data=serializer_for_upd.data, status=status.HTTP_200_OK)
#
#     # @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     # def bulk_soft_delete(self, request, *args, **kwargs):
#     #     ids = request.data.get('ids', [])
#     #     Brands.objects.filter(id__in=ids).update(is_active=False)
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#     #
#     # @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     # def bulk_restore(self, request, *args, **kwargs):
#     #     ids = request.data.get('ids', [])
#     #     Brands.objects.filter(id__in=ids).update(is_active=True)
#     #     return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return Brands.objects.filter(is_active=True)
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     filterset_fields = ['is_active', 'brand']
#     search_fields = ['brand', 'category_name']
#     ordering_fields = ['brand', 'category_name', 'is_active']
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Colors.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Colors.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return Colors.objects.filter(is_active=True)
#
#
# class ColorsViewSet(viewsets.ModelViewSet):
#     queryset = Colors.objects.all()
#     serializer_class = ColorsSerializer
#     filterset_fields = ['is_active', 'color']
#     search_fields = ['color']
#     ordering_fields = ['color', 'is_active']
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Colors.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Colors.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return Colors.objects.filter(is_active=True)
#
#
# class SizesViewSet(viewsets.ModelViewSet):
#     queryset = Sizes.objects.all()
#     serializer_class = SizesSerializer
#     filterset_fields = ['is_active', 'size']
#     search_fields = ['size']
#     ordering_fields = ['size', 'is_active']
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Sizes.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Sizes.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return Sizes.objects.filter(is_active=True)
#
#
# class GoodsViewSet(viewsets.ModelViewSet):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     filterset_fields = ['category', 'brand_id', 'color_id', 'sale_confirmed']  # Поля, по которым можно фильтровать
#     search_fields = ['model_name', 'description']  # Поля, по которым можно искать
#     ordering_fields = ['price', 'model_name']  # Поля, по которым можно сортировать
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Goods.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Goods.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return Goods.objects.filter(is_active=True)
#
#
# class HugeCardViewSet(viewsets.ModelViewSet):
#     queryset = HugeCard.objects.all()
#     serializer_class = HugeCardSerializer
#     filterset_fields = ['is_active', 'good_id']
#     search_fields = ['good_id', 'description']
#     ordering_fields = ['description', 'is_active']
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         HugeCard.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         HugeCard.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return HugeCard.objects.filter(is_active=True)
#
#
# class MainCatsViewSet(viewsets.ModelViewSet):
#     queryset = MainCats.objects.all()
#     serializer_class = MainCatsSerializer
#     filterset_fields = ['is_active', 'cat_id']
#     search_fields = ['cat_id']
#     ordering_fields = ['cat_id', 'is_active']
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         MainCats.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         MainCats.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return MainCats.objects.filter(is_active=True)
#
#
# class MainBrandsViewSet(viewsets.ModelViewSet):
#     queryset = MainBrands.objects.all()
#     serializer_class = MainBrandsSerializer
#     filterset_fields = ['is_active', 'brand_id']
#     search_fields = ['brand_id']
#     ordering_fields = ['brand_id', 'is_active']
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         MainBrands.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         MainBrands.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return MainBrands.objects.filter(is_active=True)
#
#
# class MainProductsViewSet(viewsets.ModelViewSet):
#     queryset = MainProducts.objects.all()
#     serializer_class = MainProductsSerializer
#     ilterset_fields = ['is_active', 'good_id']
#     search_fields = ['good_id']
#     ordering_fields = ['brand_id', 'good_id']
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         MainProducts.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         MainProducts.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return MainProducts.objects.filter(is_active=True)
#
#
# class SizesToGoodTableViewSet(viewsets.ModelViewSet):
#     queryset = SizesToGoodTable.objects.all()
#     serializer_class = SizesToGoodTableSerializer
#     filterset_fields = ['good', 'size', 'is_active']
#     search_fields = ['good', 'size']
#     ordering_fields = ['size', 'count', 'good', 'is_active']
#     permission_classes = [IsAuthenticated, IsAdminUser, IsDefaultUser]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         SizesToGoodTable.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated, IsAdminUser])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         SizesToGoodTable.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return SizesToGoodTable.objects.filter(is_active=True)
#
#
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     filterset_fields = ['user', 'goods', 'is_active']
#     search_fields = ['goods', 'user', 'phone_number']
#     ordering_fields = ['size', 'date_added', 'goods', 'is_active']
#     permission_classes = [
#         AllowAny
#     ]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[AllowAny])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Order.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[AllowAny])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         Order.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return Order.objects.filter(is_active=True)
#
#
# class GoodToUserViewSet(viewsets.ModelViewSet):
#     queryset = GoodToUser.objects.all()
#     serializer_class = GoodToUserSerializer
#     filterset_fields = ['order', 'good', 'is_active']
#     search_fields = ['order', 'good']
#     ordering_fields = ['order' 'good', 'is_active']
#     permission_classes = [
#         AllowAny
#     ]
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[AllowAny])
#     def bulk_soft_delete(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         GoodToUser.objects.filter(id__in=ids).update(is_active=False)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=False, methods=['PATCH'], permission_classes=[AllowAny])
#     def bulk_restore(self, request, *args, **kwargs):
#         ids = request.data.get('ids', [])
#         GoodToUser.objects.filter(id__in=ids).update(is_active=True)
#         return Response(status=status.HTTP_200_OK)
#
#     def get_queryset(self):
#         return GoodToUser.objects.filter(is_active=True)
#
#


class BrandAPIList(generics.ListCreateAPIView):
    queryset = Brands.objects.order_by('brand_name')
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = BrandFilter


class BrandAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brands.objects.filter(is_active=True)
    serializer_class = BrandSerializer


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.order_by('category_name')
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = CatsFilter


class CategoryAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class ColorsAPIList(generics.ListCreateAPIView):
    queryset = Colors.objects.order_by('color')
    serializer_class = ColorsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ColorsFilter


class ColorsAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colors.objects.filter(is_active=True)
    serializer_class = ColorsSerializer


class SizesAPIList(generics.ListCreateAPIView):
    queryset = Sizes.objects.order_by('size')
    serializer_class = ColorsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = SizesSerializer


class SizesAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sizes.objects.filter(is_active=True)
    serializer_class = SizesSerializer


class GoodsAPIList(generics.ListCreateAPIView):
    queryset = Goods.objects.order_by('model_name')
    serializer_class = GoodsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = GoodsSerializer


class GoodsAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.filter(is_active=True)
    serializer_class = GoodsSerializer


class HugeCardAPIList(generics.ListCreateAPIView):
    queryset = HugeCard.objects.order_by('description')
    serializer_class = HugeCardSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = HugeCardSerializer


class HugeCardAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = HugeCard.objects.filter(is_active=True)
    serializer_class = HugeCardSerializer


class MainCatsAPIList(generics.ListCreateAPIView):
    queryset = MainCats.objects.order_by('cat_id')
    serializer_class = MainCatsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = MainCatsSerializer


class MainCatsAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainCats.objects.filter(is_active=True)
    serializer_class = MainCatsSerializer


class MainBrandsAPIList(generics.ListCreateAPIView):
    queryset = MainBrands.objects.order_by('brand_id')
    serializer_class = MainBrandsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = MainBrandsSerializer


class MainBrandsAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainBrands.objects.filter(is_active=True)
    serializer_class = MainBrandsSerializer


class MainProductsAPIList(generics.ListCreateAPIView):
    queryset = MainProducts.objects.order_by('good_id')
    serializer_class = MainProductsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = MainProductsSerializer


class MainProductsAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainProducts.objects.filter(is_active=True)
    serializer_class = MainProductsSerializer


class SizesToGoodTableAPIList(generics.ListCreateAPIView):
    queryset = SizesToGoodTable.objects.order_by('good__model_name')
    serializer_class = SizesToGoodTableSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = SizesToGoodTableSerializer


class SizesToGoodTableAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = SizesToGoodTable.objects.filter(is_active=True)
    serializer_class = SizesToGoodTableSerializer


class OrderAPIList(generics.ListCreateAPIView):
    queryset = Order.objects.order_by('phone_number')
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderSerializer


class OrderAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.filter(is_active=True)
    serializer_class = OrderSerializer


class GoodToUserAPIList(generics.ListCreateAPIView):
    queryset = GoodToUser.objects.order_by('order__good__model_name')
    serializer_class = GoodToUserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [DjangoFilterBackend]
    filterset_class = GoodToUserSerializer


class GoodToUserAPIListAptDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodToUser.objects.filter(is_active=True)
    serializer_class = GoodToUserSerializer

# class Search(APIView):



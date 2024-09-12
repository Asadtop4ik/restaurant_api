from rest_framework import viewsets
from products.models import MenuItem, Restaurant, Category
from products.serializers import MenuItemSerializer, RestaurantSerializer, CategorySerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Menu Items'])
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    parser_classes = [MultiPartParser, FormParser]

@extend_schema(tags=['Restaurants'])
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    parser_classes = [MultiPartParser, FormParser]

@extend_schema(tags=['Categories'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, FormParser]


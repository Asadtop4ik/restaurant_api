from rest_framework import viewsets
from products.models import MenuItem, Restaurant, Menu
from products.serializers import MenuItemSerializer, RestaurantSerializer, MenuSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response


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

    @action(detail=True, methods=['get'])
    def menus(self, request, pk=None):
        restaurant = self.get_object()
        menus = Menu.objects.filter(restaurant=restaurant)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)


@extend_schema(tags=['Menus'])
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        menu = self.get_object()
        items = MenuItem.objects.filter(menu=menu)
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)
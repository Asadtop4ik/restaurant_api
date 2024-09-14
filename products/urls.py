from rest_framework import routers
from .views import MenuItemViewSet, RestaurantViewSet, CategoryViewSet, OrderViewSet, PaymentViewSet, MenuViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('menu_items', MenuItemViewSet)
router.register('restaurants', RestaurantViewSet)
router.register('categories', CategoryViewSet)
router.register('orders', OrderViewSet)
router.register('payments', PaymentViewSet)
router.register('menus', MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

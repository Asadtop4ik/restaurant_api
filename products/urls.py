from rest_framework import routers
from .views import MenuItemViewSet, RestaurantViewSet, OrderViewSet, PaymentViewSet, MenuViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('menu_items', MenuItemViewSet)
router.register('restaurants', RestaurantViewSet)
router.register('orders', OrderViewSet)
router.register('payments', PaymentViewSet)
router.register('menus', MenuViewSet)

urlpatterns = [
    path('products/orders/restaurant/<int:pk>/', OrderViewSet.as_view({'get': 'restaurant_orders'}),
         name='restaurant-orders'),
    path('', include(router.urls)),
]

from rest_framework import viewsets
from products.models import Order, Payment
from products.serializers import OrderSerializer, PaymentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response

@extend_schema(tags=['Orders'])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes = [MultiPartParser, FormParser]

    # Custom endpoint for retrieving orders by restaurant
    @action(detail=True, methods=['get'], url_path='orders')
    def restaurant_orders(self, request, pk=None):
        # Fetch orders by restaurant ID (pk is the restaurant ID)
        orders = Order.objects.filter(restaurant_id=pk)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)

@extend_schema(tags=['Payments'])
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    parser_classes = [MultiPartParser, FormParser]


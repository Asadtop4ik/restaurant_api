from rest_framework import viewsets
from products.models import Order, Payment
from products.serializers import OrderSerializer, PaymentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Orders'])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes = [MultiPartParser, FormParser]

@extend_schema(tags=['Payments'])
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    parser_classes = [MultiPartParser, FormParser]


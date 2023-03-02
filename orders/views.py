from rest_framework import generics
from .models import Order, ProductsInOrder
from rest_framework.permissions import  IsAuthenticated

from .serializers import OrderSerializer, PrInOrderSerializer
# Create your views here.

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


class PrInOrderView(generics.ListCreateAPIView):
    queryset = ProductsInOrder.objects.all()
    serializer_class = PrInOrderSerializer
    permission_classes = (IsAuthenticated,)

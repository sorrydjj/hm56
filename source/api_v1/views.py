from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly, IsAdminUser, \
    DjangoModelPermissionsOrAnonReadOnly
from webapp.models import Product, Order, OrderProduct
from api_v1.serializers import ProductSerializer, OrderSerializer, OrderProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | DjangoModelPermissionsOrAnonReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

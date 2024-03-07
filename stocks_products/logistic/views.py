from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['title', 'description']
    search_fields = ['title', 'description']

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['address', 'products']
    search_fields = ['address', 'products']
    # при необходимости добавьте параметры фильтрации

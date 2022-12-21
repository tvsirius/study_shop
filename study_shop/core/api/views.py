from rest_framework import viewsets
from study_shop.core.models import Clothes, Category, Suppliers
from .serializers import ClothesSerializer, CategorySerializer, SuppliersSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = {
                            'title':['exact', 'icontains', 'startswith', 'endswith'],
                            'manufacturer':['exact', 'icontains', 'startswith', 'endswith'],
                            'price':['exact', 'lte', 'gte'],
                            'size':['exact'],
                            'discount':['exact', 'lte', 'gte'],
                            'is_available':['exact'],
                            'category':['exact'],
                            'season': ['exact'],
                            'supplier':['exact'],
    }
    search_fields = {
        'title',
        'manufacturer',
    }



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter)



class SuppliersViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    filterset_fields = "__all__"
    search_fields = "__all__"




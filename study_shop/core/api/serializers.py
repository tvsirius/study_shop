from rest_framework import serializers
from study_shop.core.models import Clothes, Category, Suppliers

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = "__all__"


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = "__all__"


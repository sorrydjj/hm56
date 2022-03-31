from rest_framework import serializers, generics

from webapp.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("names",)


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ("id", "name", "descriptions", "category", "count", "price")
        read_only_fields = ("id",)
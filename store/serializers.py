from rest_framework import serializers
from .models import Product, Category, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Category.objects.all(),
        source='category'
    )

    class Meta:
        model = Product
        fields = ['id',
        'title',
        'slug',
        'description',
        'price',
        'category',
        'category_id',
        'image',
        'inventory',
        "stock_status",
            "is_active",
            "created_at",
            "updated_at",]
read_only_fields = ["slug", "stock_status", "created_at", "updated_at"]
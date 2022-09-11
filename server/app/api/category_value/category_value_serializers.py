from rest_framework import serializers
from .models import CategoryValueModel
from ..category.category_serializers import CategorySerializers


class CategoryValueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryValueModel
        exclude = ['created_at', "updated_at"]


class CategoryValueSerializer(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = CategoryValueModel
        exclude = ['created_at', "updated_at"]
        depth = 1

from rest_framework import serializers
from .models import CategoryValueModel


class CategoryValueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryValueModel
        fields = ["id", "name", "category"]


class CategoryValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryValueModel
        fields = ["id", "name", "category"]
        depth = 1

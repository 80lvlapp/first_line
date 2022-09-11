from rest_framework import serializers
from .models import CategoryModel


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['created_at', "updated_at"]

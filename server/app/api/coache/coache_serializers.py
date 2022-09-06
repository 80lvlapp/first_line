from rest_framework import serializers
from .models import CoacheModel


class CoacheSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoacheModel
        fields = ["id", "name"]

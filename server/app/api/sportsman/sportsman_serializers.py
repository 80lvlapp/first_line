from rest_framework import serializers
from .models import SportsmanModel


class SportsmanSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportsmanModel
        exclude = ['created_at', "updated_at"]

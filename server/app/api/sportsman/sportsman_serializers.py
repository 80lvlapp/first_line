from rest_framework import serializers
from .models import SportsmanModel


class SportsmanSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportsmanModel
        fields = "__all__"

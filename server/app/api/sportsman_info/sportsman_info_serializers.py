from rest_framework import serializers
from .models import SportsmanInfoModel


class SportsmanInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportsmanInfoModel
        fields = "__all__"
        depth = 1


class SportsmanInfoCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportsmanInfoModel
        fields = ['period', "sport_school", "sportsman", "coache", "insuranse"]

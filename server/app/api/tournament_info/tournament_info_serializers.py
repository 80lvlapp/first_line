from rest_framework import serializers
from .models import TournamentInfoModel


class TournamentInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TournamentInfoModel
        fields = "__all__"
        depth = 2


class TournamentInfoCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = TournamentInfoModel
        fields = ['period', "tournament", "sportsman", "category_value", "points"]

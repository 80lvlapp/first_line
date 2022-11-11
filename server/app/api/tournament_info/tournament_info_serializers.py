from rest_framework import serializers
from .models import TournamentInfoModel
from ..category_value.category_value_serializers import CategoryValueCreateSerializer
from ..sportsman.sportsman_serializers import SportsmanSerializers
from ..tournament.tournament_serializers import TournamentSerializers


class TournamentInfoSerializers(serializers.ModelSerializer):
    tournament = TournamentSerializers()
    sportsman = SportsmanSerializers()
    category_value = CategoryValueCreateSerializer()

    class Meta:
        model = TournamentInfoModel
        exclude = ['created_at', "updated_at"]
        depth = 2


class TournamentInfoCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = TournamentInfoModel
        fields = ['period', "tournament",
                  "sportsman", "category_value", "points", "place"]


class TournamentInfoReportSerializers(serializers.ModelSerializer):
    sportsman = SportsmanSerializers()

    class Meta:
        model = TournamentInfoModel
        fields = ["period", "sportsman", "points"]


class TournamentSportsmanReportInfoReportSerializers(serializers.ModelSerializer):
    tournament = TournamentSerializers()
    class Meta:
        model = TournamentInfoModel
        fields = ["period", "tournament"]
        depth = 1

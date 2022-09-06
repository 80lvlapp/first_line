from rest_framework import serializers
from .models import ScoreScaleModel


class ScoreScaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScoreScaleModel
        fields = "__all__"
        depth = 1


class ScoreScaleCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScoreScaleModel
        fields = ['period', "sport_school", "type_tournament", "place_from", "place_to", "numbers_of_points"]

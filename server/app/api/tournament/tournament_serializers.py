from rest_framework import serializers
from .models import TournamentModel


class TournamentSerializers(serializers.ModelSerializer):
    class Meta:
        model = TournamentModel
        fields = "__all__"
        depth = 1


class TournamentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = TournamentModel
        fields = ['id', "name", "date_tournament", "venue", "type_of_tornament"]

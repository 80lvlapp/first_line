from rest_framework import serializers
from .models import TournamentModel
from ..type_of_tournament.type_of_tournamet_serializers import TypeOfTournametSerializers


class TournamentSerializers(serializers.ModelSerializer):
    type_of_tornament = TypeOfTournametSerializers()

    class Meta:
        model = TournamentModel
        exclude = ['created_at', "updated_at"]
        depth = 1


class TournamentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = TournamentModel
        exclude = ['created_at', "updated_at"]

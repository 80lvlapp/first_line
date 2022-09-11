from rest_framework import serializers
from .models import TypeOfTournamentModel


class TypeOfTournametSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeOfTournamentModel
        fields = ["id", "name"]

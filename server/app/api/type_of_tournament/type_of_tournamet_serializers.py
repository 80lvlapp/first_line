from rest_framework import serializers
from .models import TypeOfTournamentModel


class TypeOfTournametSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeOfTournamentModel
        exclude = ['created_at', "updated_at"]

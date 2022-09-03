from rest_framework import serializers
from .models import SportSchoolModel


class SportSchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportSchoolModel
        fields = ["id", "name"]

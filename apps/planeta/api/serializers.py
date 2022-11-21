from rest_framework import serializers
from apps.planeta.models import Planeta


class PlanetaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Planeta
        fields='__all__'
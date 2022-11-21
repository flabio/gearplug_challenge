from rest_framework import serializers
from apps.pelicula.models import Pelicula
from apps.planeta.api.serializers import PlanetaSerializer

class PeliculaSerializer(serializers.ModelSerializer):
    planetalista=PlanetaSerializer(many=True,read_only=True)
    class Meta:
        model=Pelicula
        fields='__all__'
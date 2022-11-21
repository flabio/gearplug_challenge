from rest_framework import serializers
from apps.personaje.models import Personaje
from apps.pelicula.api.serializers import PeliculaSerializer

class PersonajeSerializer(serializers.ModelSerializer):
    peliculaslistas=PeliculaSerializer(many=True,read_only=True)
    class Meta:
        model=Personaje
        fields='__all__'
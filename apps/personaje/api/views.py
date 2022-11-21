from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from apps.personaje.models import Personaje
from apps.personaje.api.serializers import PersonajeSerializer

class PersonajeList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = PersonajeSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['full_name']
    def get_queryset(self):
        return Personaje.objects.filter()

class PersonajeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
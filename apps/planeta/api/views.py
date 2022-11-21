from rest_framework import generics
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from apps.planeta.models import Planeta
from apps.planeta.api.serializers import PlanetaSerializer

class PlanetList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = PlanetaSerializer
    def get_queryset(self):
        return Planeta.objects.filter()

class PlanetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer
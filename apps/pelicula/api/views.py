from rest_framework import generics
from rest_framework.response import Response
from  rest_framework.permissions import IsAuthenticated
from apps.pelicula.models import Pelicula
from apps.pelicula.api.serializers import PeliculaSerializer

class PeliculaList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = PeliculaSerializer

    def get_queryset(self):
        return Pelicula.objects.filter()

class PeliculaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
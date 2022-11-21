from django.db import models
from apps.personaje.models import Personaje
# Create your models here.
class Pelicula(models.Model):
    name=models.CharField(max_length=250)
    apertura=models.CharField(max_length=250)
    director=models.CharField(max_length=250)
    prodcutora=models.CharField(max_length=250)
    active=models.BooleanField(default=True)
    personaje=models.ForeignKey(Personaje,on_delete=models.CASCADE,related_name='peliculaslistas')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'

from django.db import models
from apps.pelicula.models import Pelicula
# Create your models here.
class Planeta(models.Model):
    name=models.CharField(max_length=250)
    active=models.BooleanField(default=True)
    pelicula=models.ForeignKey(Pelicula,on_delete=models.CASCADE,related_name="planetalista")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
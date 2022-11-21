from django.db import models

# Create your models here.
class Personaje(models.Model):
    full_name=models.CharField(max_length=250,unique=True)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.full_name}'
# Generated by Django 4.1.3 on 2022-11-19 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personaje', '0001_initial'),
        ('planeta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('apertura', models.CharField(max_length=250)),
                ('director', models.CharField(max_length=250)),
                ('prodcutora', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('planeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planetalista', to='planeta.planeta')),
            ],
        ),
        migrations.CreateModel(
            name='PeliculaPersonaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peliculalista', to='pelicula.pelicula')),
                ('personaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personajelista', to='personaje.personaje')),
            ],
        ),
    ]

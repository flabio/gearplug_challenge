# Generated by Django 4.1.3 on 2022-11-19 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='full_name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
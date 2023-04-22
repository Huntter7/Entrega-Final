# Generated by Django 4.1.7 on 2023-04-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kepler', '0008_profile_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='descripcion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='encabezado',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='texto_descriptivo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pequeña_introduccion',
            field=models.CharField(max_length=150),
        ),
    ]

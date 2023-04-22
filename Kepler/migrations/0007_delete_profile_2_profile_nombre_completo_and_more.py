# Generated by Django 4.1.7 on 2023-04-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kepler', '0006_profile_2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile_2',
        ),
        migrations.AddField(
            model_name='profile',
            name='nombre_completo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='pequeña_introduccion',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]

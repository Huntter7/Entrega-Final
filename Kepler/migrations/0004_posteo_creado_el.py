# Generated by Django 4.1.7 on 2023-04-13 00:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Kepler', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='creado_el',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

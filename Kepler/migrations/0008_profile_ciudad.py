# Generated by Django 4.1.7 on 2023-04-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kepler', '0007_delete_profile_2_profile_nombre_completo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ciudad',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

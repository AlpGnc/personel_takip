# Generated by Django 5.1.3 on 2024-11-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kullanici', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='is_yetkili',
            field=models.BooleanField(default=False),
        ),
    ]

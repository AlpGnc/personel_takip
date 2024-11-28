# Generated by Django 5.1.3 on 2024-11-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='izin',
            name='durum',
        ),
        migrations.AddField(
            model_name='izin',
            name='onay_durumu',
            field=models.CharField(choices=[('Bekliyor', 'Bekliyor'), ('Onaylandı', 'Onaylandı'), ('Reddedildi', 'Reddedildi')], default='Bekliyor', max_length=20),
        ),
    ]
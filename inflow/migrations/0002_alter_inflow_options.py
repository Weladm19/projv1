# Generated by Django 5.1.4 on 2024-12-24 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inflow',
            options={'ordering': ['-data_lancamento']},
        ),
    ]

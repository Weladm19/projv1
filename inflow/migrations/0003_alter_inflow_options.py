# Generated by Django 5.1.4 on 2025-01-16 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflow', '0002_alter_inflow_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inflow',
            options={'ordering': ['produto']},
        ),
    ]

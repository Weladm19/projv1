# Generated by Django 5.1.4 on 2025-01-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area_vendedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venloja',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]

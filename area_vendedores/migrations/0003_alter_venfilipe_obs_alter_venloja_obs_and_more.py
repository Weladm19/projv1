# Generated by Django 5.1.4 on 2025-01-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area_vendedores', '0002_alter_venfilipe_valor_alter_ventoninho_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venfilipe',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='venloja',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ventoninho',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]

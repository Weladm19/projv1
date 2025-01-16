# Generated by Django 5.1.4 on 2025-01-14 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0002_alter_produto_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenFilipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantidade', models.IntegerField()),
                ('obs', models.TextField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VenLoja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True)),
                ('quantidade', models.IntegerField()),
                ('obs', models.TextField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VenToninho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantidade', models.IntegerField()),
                ('obs', models.TextField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

# Generated by Django 5.1 on 2024-08-24 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Estado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CidadeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cidades', to='Estado.estadomodel')),
            ],
        ),
    ]

# Generated by Django 5.1 on 2024-08-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estado', '0002_alter_estadomodel_sigla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadomodel',
            name='sigla',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]

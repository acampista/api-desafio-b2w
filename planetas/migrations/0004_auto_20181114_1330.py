# Generated by Django 2.1.3 on 2018-11-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planetas', '0003_auto_20181114_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeta',
            name='id_swapi',
            field=models.IntegerField(),
        ),
    ]

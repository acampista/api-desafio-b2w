# Generated by Django 2.1.3 on 2018-11-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planetas', '0004_auto_20181114_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeta',
            name='id_swapi',
            field=models.IntegerField(null=True),
        ),
    ]

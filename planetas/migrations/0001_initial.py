# Generated by Django 2.1.3 on 2018-11-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('clima', models.CharField(max_length=100)),
                ('terreno', models.CharField(max_length=100)),
                ('QtdAparicoes', models.IntegerField()),
            ],
        ),
    ]

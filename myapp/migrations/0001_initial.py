# Generated by Django 3.2.18 on 2023-03-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.IntegerField(default=0)),
                ('d2', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EnergyMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.IntegerField(default=0)),
                ('volt', models.IntegerField(default=0)),
                ('current', models.FloatField(default=0.0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

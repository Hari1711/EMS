# Generated by Django 3.2.18 on 2023-03-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devices',
            old_name='d1',
            new_name='dev',
        ),
        migrations.RemoveField(
            model_name='devices',
            name='d2',
        ),
        migrations.AddField(
            model_name='devices',
            name='status',
            field=models.CharField(default='Off', max_length=10),
        ),
    ]
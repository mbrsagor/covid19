# Generated by Django 3.0.7 on 2020-06-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20200622_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='availability',
            name='time',
            field=models.TimeField(),
        ),
    ]

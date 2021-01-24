# Generated by Django 3.0.7 on 2020-08-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_help_help_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='disease_image',
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_availability',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
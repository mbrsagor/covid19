# Generated by Django 3.0.7 on 2020-06-30 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('hospital', '0006_auto_20200622_1647'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='roles',
            field=models.ManyToManyField(to='user.Role'),
        ),
    ]
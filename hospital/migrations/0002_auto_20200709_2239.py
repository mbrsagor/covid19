# Generated by Django 3.0.7 on 2020-07-09 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='username',
            new_name='user',
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-04 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disease_name', models.CharField(max_length=120)),
                ('disease_image', models.ImageField(blank=True, null=True, upload_to='disease/%y/%m')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=70)),
                ('help_text', models.CharField(max_length=110)),
                ('help_image', models.ImageField(blank=True, null=True, upload_to='help//%y/%m')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital_name', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=200)),
                ('hospital_type', models.CharField(choices=[('Governmental', 'Governmental'), ('Private', 'Private')], default='Governmental', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=95)),
                ('flag', models.ImageField(blank=True, null=True, upload_to='flag/%y/%m')),
                ('is_active', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Contagion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('daily_test', models.IntegerField(default=0)),
                ('daily_effected', models.IntegerField(default=0)),
                ('daily_dies', models.IntegerField(default=0)),
                ('daily_recovery', models.IntegerField(default=0)),
                ('is_publish', models.BooleanField(blank=True, default=True, null=True)),
                ('date_time', models.DateField(blank=True, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CountryName', to='core.Location')),
                ('disease', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ContagionName', to='core.Disease')),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

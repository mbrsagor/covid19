# Generated by Django 3.0.7 on 2020-07-08 18:41

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
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Doctor', 'doctor'), ('Nurse', 'nurse'), ('Laboratories', 'laboratories'), ('Accountant', 'accountant'), ('HR', 'hr'), ('ADMIN', 'admin')], max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='users_role', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(null=True, upload_to='profile/%Y/%m/')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Birth Date')),
                ('gender', models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE'), ('Other', 'OTHER')], default='Male', max_length=16)),
                ('mobile', models.CharField(max_length=16, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=95, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

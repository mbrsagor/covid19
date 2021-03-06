# Generated by Django 3.0.7 on 2020-07-09 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('day', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department_name', models.CharField(max_length=80)),
                ('employee_type', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('specialization', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=120)),
                ('phone_number', models.IntegerField(default=0)),
                ('education', models.TextField()),
                ('date_of_birth', models.DateTimeField()),
                ('visit_fee', models.IntegerField(default=0)),
                ('designation', models.CharField(max_length=70)),
                ('profile_photo', models.ImageField(upload_to='doctor')),
                ('gender', models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE'), ('Other', 'OTHER')], default='Male', max_length=10)),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_availability', to='hospital.Availability')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_department', to='hospital.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization_name', models.CharField(max_length=120)),
                ('designation', models.CharField(max_length=70)),
                ('job_year', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laboratories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lab_name', models.CharField(max_length=120)),
                ('machinery_name', models.CharField(blank=True, max_length=150, null=True)),
                ('total_machinery', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.TimeField()),
                ('phone_number', models.IntegerField(default=0)),
                ('profile_photo', models.ImageField(upload_to='patient')),
                ('age', models.ImageField(upload_to='', verbose_name=0)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('postal_code', models.IntegerField(default=0)),
                ('date_of_birth', models.DateTimeField()),
                ('reference_name', models.CharField(blank=True, max_length=70, null=True)),
                ('reference_phone_number', models.ImageField(default=0, upload_to='')),
                ('gender', models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE'), ('Other', 'OTHER')], default='Male', max_length=10)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PatientProfile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=1)),
                ('discount_price', models.IntegerField(default=0)),
                ('laboratories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_laboratories', to='hospital.Laboratories')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_name', models.CharField(max_length=120)),
                ('patient_name', models.CharField(blank=True, max_length=70, null=True)),
                ('address', models.CharField(blank=True, max_length=70, null=True)),
                ('phone_number', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_patient_name', to='hospital.Patient')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_service', to='hospital.Service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('available_days', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('message', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('doctor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_schedule', to='hospital.Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_experience', to='hospital.Experience'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_role', to='user.Role'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='DoctorProfile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=90)),
                ('phn_number', models.IntegerField(default=0)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('problem', models.TextField(blank=True, null=True)),
                ('address', models.TextField()),
                ('Department_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_appointment', to='hospital.Department')),
                ('schedules', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_schedules', to='hospital.Schedule')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

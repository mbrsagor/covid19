from django.db import models
from django.contrib.auth.models import User
from contagion.helpers.enums import *
from contagion.models import BaseEntity, Disease


# Create your models here.
class Experience(BaseEntity):
    organization_name = models.CharField(max_length=120)
    designation = models.CharField(max_length=70)
    job_year = models.CharField(max_length=70)

    def __str__(self):
        return self.organization_name


class Schedule(BaseEntity):
    day = models.CharField(max_length=50)
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.day


class Department(BaseEntity):
    department_name = models.CharField(max_length=80)
    employee_type = models.CharField(max_length=120)

    def __str__(self):
        return self.employee_type


class Doctor(BaseEntity):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='DoctorProfile')
    specialist = models.CharField(max_length=100)
    location = models.CharField(max_length=120)
    phone_number = models.IntegerField(default=0)
    education = models.TextField()
    visit_fee = models.IntegerField(default=0)
    designation = models.CharField(max_length=70)
    profile_photo = models.ImageField(upload_to='doctor')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employee_department')
    availability = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True, related_name='doctor_schedule')
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='doctor_experience')
    gender = models.CharField(choices=GenderEnum.choices(), default=GenderEnum.MALE.value, max_length=10)

    def __str__(self):
        return self.username.username


class Patient(BaseEntity):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='PatientProfile')
    address = models.TimeField()
    phone_number = models.IntegerField(default=0)
    profile_photo = models.ImageField(upload_to='patient')
    age = models.ImageField(0)
    city = models.CharField(max_length=120, blank=True, null=True)
    reference_name = models.CharField(max_length=70, blank=True, null=True)
    reference_phone_number = models.ImageField(default=0)
    gender = models.CharField(choices=GenderEnum.choices(), default=GenderEnum.MALE.value, max_length=10)

    def __str__(self):
        return self.username.username

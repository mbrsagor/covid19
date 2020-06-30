from django.db import models
from django.contrib.auth.models import User
from contagion.helpers.enums import *
from contagion.models import BaseEntity, Disease
from user.models import Role


# Create your models here.
class Experience(BaseEntity):
    organization_name = models.CharField(max_length=120)
    designation = models.CharField(max_length=70)
    job_year = models.CharField(max_length=70)

    def __str__(self):
        return self.organization_name


class Availability(BaseEntity):
    day = models.CharField(max_length=50)
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.day


class Laboratories(BaseEntity):
    lab_name = models.CharField(max_length=120)
    machinery_name = models.CharField(max_length=150, blank=True, null=True)
    total_machinery = models.IntegerField(default=1)

    def __str__(self):
        return self.lab_name


class Department(BaseEntity):
    department_name = models.CharField(max_length=80)
    employee_type = models.CharField(max_length=120)

    def __str__(self):
        return self.employee_type


class Service(BaseEntity):
    service_name = models.CharField(max_length=100)
    price = models.IntegerField(default=1)
    discount_price = models.IntegerField(default=0)
    laboratories = models.ForeignKey(Laboratories, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='service_laboratories')

    def __str__(self):
        return self.service_name


class Doctor(BaseEntity):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='DoctorProfile')
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=120)
    phone_number = models.IntegerField(default=0)
    education = models.TextField()
    date_of_birth = models.DateTimeField(auto_now_add=False)
    visit_fee = models.IntegerField(default=0)
    designation = models.CharField(max_length=70)
    roles = models.ManyToManyField(Role)
    profile_photo = models.ImageField(upload_to='doctor')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employee_department')
    availability = models.ForeignKey(Availability, on_delete=models.SET_NULL, null=True,
                                     related_name='doctor_availability')
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
    postal_code = models.IntegerField(default=0)
    date_of_birth = models.DateTimeField(auto_now_add=False)
    reference_name = models.CharField(max_length=70, blank=True, null=True)
    reference_phone_number = models.ImageField(default=0)
    gender = models.CharField(choices=GenderEnum.choices(), default=GenderEnum.MALE.value, max_length=10)

    def __str__(self):
        return self.username.username


class Schedule(BaseEntity):
    doctor_name = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='doctor_schedule')
    available_days = models.CharField(max_length=50)
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)
    message = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.doctor_name.username


class Appointment(BaseEntity):
    name = models.CharField(max_length=90)
    Department_name = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,
                                        related_name='doctor_appointment')

    schedules = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True, related_name='doctor_schedules')
    phn_number = models.IntegerField(default=0)
    email = models.EmailField(blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class Test(BaseEntity):
    test_name = models.CharField(max_length=120)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='test_patient_name')
    patient_name = models.CharField(max_length=70, blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    phone_number = models.IntegerField(default=0)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='test_service')

    def __str__(self):
        return self.test_name

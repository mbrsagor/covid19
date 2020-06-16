from django.db import models
from django.contrib.auth.models import User
from .helpers.enums import *


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Location(BaseEntity):
    name = models.CharField(max_length=95)
    flag = models.ImageField(upload_to='flag/%y/%m', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_children(self):
        return Location.objects.filter(parent=self)

    def children_count(self):
        return Location.objects.filter(parent=self).count()


class Profile(BaseEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    email = models.EmailField()
    photo = models.ImageField(upload_to='profile/%Y/%m/', null=True)
    date_of_birth = models.DateField(verbose_name="Birth Date", null=True)
    gender = models.CharField(choices=GenderEnum.choices(), default=GenderEnum.MALE.value, max_length=16)
    mobile = models.CharField(max_length=16, unique=True, null=True, blank=False)
    address = models.CharField(max_length=95, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def name(self):
        try:
            return self.user.username
        except AttributeError:
            return 'N/A'


class Disease(BaseEntity):
    disease_name = models.CharField(max_length=120)
    disease_image = models.ImageField(upload_to='disease/%y/%m', null=True, blank=True)

    def __str__(self):
        return self.disease_name


class Contagion(BaseEntity):
    disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True, related_name='ContagionName')
    country = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name='CountryName')
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author')
    daily_test = models.IntegerField(default=0)
    daily_effected = models.IntegerField(default=0)
    daily_dies = models.IntegerField(default=0)
    daily_recovery = models.IntegerField(default=0)
    is_publish = models.BooleanField(blank=True, null=True, default=True)
    date_time = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.disease.disease_name


class Help(BaseEntity):
    title = models.CharField(max_length=70)
    help_text = models.CharField(max_length=110)
    help_image = models.ImageField(upload_to='help//%y/%m', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Hospital(BaseEntity):
    hospital_name = models.CharField(max_length=120)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.hospital_name

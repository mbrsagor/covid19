from django.db import models
from django.conf import settings
from core.helpers.enums import *
from core.models.base import BaseEntity

ROLE_CHOICE = (
    ('Doctor', 'doctor'),
    ('Nurse', 'nurse'),
    ('Laboratories', 'laboratories'),
    ('Accountant', 'accountant'),
    ('HR', 'hr'),
    ('ADMIN', 'admin'),
)


class Role(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_query_name="users_role")
    role = models.CharField(max_length=30, choices=ROLE_CHOICE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.role


class Profile(BaseEntity):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_profile")
    email = models.EmailField()
    photo = models.ImageField(upload_to='profile/%Y/%m/', null=True)
    date_of_birth = models.DateField(verbose_name="Birth Date", null=True)
    gender = models.CharField(choices=GenderEnum.choices(), default=GenderEnum.MALE.value, max_length=16)
    mobile = models.CharField(max_length=16, unique=True, null=True, blank=False)
    address = models.CharField(max_length=95, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

    @property
    def name(self):
        try:
            return self.email
        except AttributeError:
            return 'N/A'

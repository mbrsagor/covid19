from django.db import models
from django.conf import settings

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

from django.db import models
from core.models.base import BaseEntity
from hospital.models.Patient import Patient
from hospital.models.management import Service


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

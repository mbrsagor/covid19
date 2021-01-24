from hospital.models.appointment import Appointment
from hospital.serializers.appointment_serializer import AppointmentSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, ]

from .models import *
from .serializers import *
from .permissions import *
from user.serializers import UserSerializer

from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class AvailabilityViewSet(ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer


class LaboratoriesViewSet(ModelViewSet):
    queryset = Laboratories.objects.all()
    serializer_class = LaboratoriesSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class DoctorAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            queryset = Doctor.objects.get(id=self.request.user.id)
            serializer = DoctorSerializer(queryset)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            queryset = User.objects.get(id=self.request.user.id)
            serializer = UserSerializer(queryset)
            return Response(serializer.data, status=HTTP_200_OK)

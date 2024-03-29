from hospital.models.management import *
from hospital.serializers.management_serializer import *
from hospital.permissions.permissions import PermissionHelperMixin

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser


class ExperienceViewSet(ModelViewSet, PermissionHelperMixin):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_permissions(self):
        return self.admin_editable_only()


class AvailabilityViewSet(ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = (IsAdminUser, )


class LaboratoriesViewSet(ModelViewSet):
    queryset = Laboratories.objects.all()
    serializer_class = LaboratoriesSerializer
    permission_classes = (IsAdminUser,)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = (IsAdminUser,)


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = (IsAdminUser,)

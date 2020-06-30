from .models import *
from .serializers import *
from hospital.permissions import *

from rest_framework.viewsets import ModelViewSet


class RoleViewSet(ModelViewSet, PermissionHelperMixin):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)

    def get_permissions(self):
        return self.admin_editable_only()

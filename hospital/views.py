from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

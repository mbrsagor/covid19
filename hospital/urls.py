from .views import *from rest_framework import routersfrom django.urls import path, includerouter = routers.DefaultRouter()router.register('experience', ExperienceViewSet)router.register('availability', AvailabilityViewSet)router.register('laboratories', LaboratoriesViewSet)router.register('department', DepartmentViewSet)router.register('service', ServiceViewSet)urlpatterns = [    path('', include(router.urls)),]

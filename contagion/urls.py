from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('disease', DiseaseViewSet)
router.register('help', HelpViewSet)
router.register('hospital', HospitalViewSet)

urlpatterns = [
    path('api/location/', LocationApiView.as_view(), name='country'),
    path('api/location/<int:id>/', LocationUpdateDeleteView.as_view(), name='country-update'),
    path('api/contagion/', ContagionApiView.as_view(), name='Contagion'),
    path('api/contagion/<int:id>/', ContagionUpdateDeleteView.as_view(), name='Contagion-update'),
    path('api/', include(router.urls)),
]

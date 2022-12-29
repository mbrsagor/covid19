from django.urls import path, include
from rest_framework import routers

from core.views.contagion_view import *
from core.views.home_views import HomeView

router = routers.DefaultRouter()
router.register('disease', DiseaseViewSet)
router.register('help', HelpViewSet)
router.register('hospital', HospitalViewSet)

urlpatterns = [
    # Location endpoint
    path('api/location/', LocationApiView.as_view()),
    path('api/location/<int:id>/', LocationUpdateDeleteView.as_view()),
    # Contagion endpoint
    path('api/contagion/', ContagionApiView.as_view()),
    path('api/contagion/<int:id>/', ContagionUpdateDeleteView.as_view()),
    path('api/', include(router.urls)),
    path('', HomeView.as_view(), name='home'),
]

from .views import *from rest_framework import routersrouter = routers.DefaultRouter()router.register('role', RoleViewSet)urlpatterns = router.urls
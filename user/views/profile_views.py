from hospital.permissions.permissions import *from user.models.profile import *from user.serializers.profile_serializer import *from django.contrib.auth.models import Userfrom rest_framework.viewsets import ModelViewSetfrom rest_framework.permissions import IsAuthenticatedfrom rest_framework.views import APIViewfrom rest_framework.response import Responsefrom rest_framework.status import HTTP_200_OKclass RoleViewSet(ModelViewSet, PermissionHelperMixin):    queryset = Role.objects.all()    serializer_class = RoleSerializer    def perform_create(self, serializer):        return serializer.save(user=self.request.user)    def perform_update(self, serializer):        return serializer.save(user=self.request.user)    def get_permissions(self):        return self.admin_editable_only()class ProfileAPIIView(APIView):    permission_classes = [IsAuthenticated]    def get(self, request):        try:            queryset = Profile.objects.get(id=self.request.user.id)            serializer = ProfileSerializer(queryset)            return Response(serializer.data, status=HTTP_200_OK)        except Exception as e:            queryset = User.objects.get(id=self.request.user.id)            serializer = UserSerializer(queryset)            return Response(serializer.data, status=HTTP_200_OK)class UserModelViewSet(ModelViewSet, PermissionHelperMixin):    queryset = User.objects.all()    serializer_class = UserSerializer    def get_permissions(self):        return self.admin_editable_only()
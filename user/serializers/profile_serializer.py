from django.contrib.auth.models import Userfrom rest_framework.serializers import ModelSerializerfrom user.models.profile import *class UserSerializer(ModelSerializer):    class Meta:        model = User        fields = ('id', 'username', 'email')class RoleSerializer(ModelSerializer):    class Meta:        model = Role        fields = (            'id', 'user', 'role', 'created_date'        )    def to_representation(self, instance):        response = super().to_representation(instance)        response['user'] = UserSerializer(instance.user).data        return responseclass ProfileSerializer(ModelSerializer):    class Meta:        model = Profile        fields = [            'id', 'user', 'email', 'photo',            'date_of_birth', 'gender', 'mobile', 'address', 'bio',            'created_at', 'updated_at'        ]    def to_representation(self, instance):        response = super().to_representation(inspect)        response['user'] = UserSerializer(inspect.user).data        return response
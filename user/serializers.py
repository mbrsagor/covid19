from .models import *from rest_framework.serializers import ModelSerializerclass RoleSerializer(ModelSerializer):    class Meta:        model = Role        fields = (            'id', 'user', 'role', 'created_date'        )
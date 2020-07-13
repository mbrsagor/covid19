from hospital.models.doctor import Doctorfrom user.serializers.profile_serializer import UserSerializerfrom hospital.serializers.management_serializer import AvailabilitySerializerfrom rest_framework.serializers import ModelSerializerclass DoctorSerializer(ModelSerializer):    class Meta:        model = Doctor        fields = (            'id', 'user', 'specialization', 'address', 'phone_number', 'education',            'date_of_birth', 'visit_fee', 'designation', 'roles', 'profile_photo',            'department', 'availability', 'experience', 'gender', 'created_at', 'updated_at'        )        read_only_fields = ['user']        # depth = 1    def to_representation(self, instance):        response = super().to_representation(instance)        response['user'] = UserSerializer(instance.user).data        return response
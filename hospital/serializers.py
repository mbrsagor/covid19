from .models import *from rest_framework.serializers import ModelSerializerclass ExperienceSerializer(ModelSerializer):    class Meta:        model = Experience        fields = (            '__all__'        )class AvailabilitySerializer(ModelSerializer):    class Meta:        model = Availability        fields = (            '__all__'        )class LaboratoriesSerializer(ModelSerializer):    class Meta:        model = Laboratories        fields = (            '__all__'        )class DepartmentSerializer(ModelSerializer):    class Meta:        model = Department        fields = (            '__all__'        )class ServiceSerializer(ModelSerializer):    class Meta:        model = Service        fields = (            '__all__'        )    def to_representation(self, instance):        response = super().to_representation(instance)        response['laboratories'] = LaboratoriesSerializer(instance.laboratories).data        return responseclass DoctorSerializer(ModelSerializer):    class Meta:        model = Doctor        fields = {            '__all__'        }
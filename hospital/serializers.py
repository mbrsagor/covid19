from .models import *from rest_framework.serializers import ModelSerializerclass ExperienceSerializer(ModelSerializer):    class Meta:        model = Experience        fields = (            '__all__'        )class AvailabilitySerializer(ModelSerializer):    class Meta:        model = Availability        fields = (            '__all__'        )class LaboratoriesSerializer(ModelSerializer):    class Meta:        model = Laboratories        fields = (            '__all__'        )
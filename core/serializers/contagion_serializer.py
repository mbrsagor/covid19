from core.models.contagion import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id', 'name', 'flag',
            'is_active', 'created_at', 'updated_at'
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            '__all__'
        )


class DiseaseSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = [
            'id', 'disease_name', 'disease_fee',
            'disease_availability', 'created_at', 'updated_at'
        ]


class ContagionSerializer(ModelSerializer):
    class Meta:
        model = Contagion
        fields = [
            'id', 'disease', 'country', 'reporter', 'daily_test',
            'daily_effected', 'daily_dies', 'daily_recovery',
            'is_publish', 'date_time', 'created_at', 'updated_at'
        ]

        read_only_field = ['reporter']


class HelpSerializer(ModelSerializer):
    class Meta:
        model = Help
        fields = [
            'id', 'title', 'help_text',
            'help_image', 'created_at', 'updated_at'
        ]


class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = [
            'id', 'hospital_name', 'location', 'hospital_type'
        ]

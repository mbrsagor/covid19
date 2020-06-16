from .models import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id', 'name', 'parent', 'flag',
            'is_active', 'created_at', 'updated_at'
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            '__all__'
        )


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'email', 'photo',
            'date_of_birth', 'gender', 'mobile', 'address', 'bio',
            'created_at', 'updated_at'
        ]

    def to_representation(self, instance):
        response = super().to_representation(inspect)
        response['user'] = UserSerializer(inspect.user).data
        return response


class DiseaseSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = [
            'id', 'disease_name', 'disease_image',
            'created_at', 'updated_at'
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
            'id', 'hospital_name', 'location'
        ]

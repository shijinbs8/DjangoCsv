from .models import *
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'age']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_email(self, value):
        value = value.strip()
        if UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists.")
        return value

    def validate_age(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("Age must be an integer.")
        if value < 0 or value > 120:
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return value
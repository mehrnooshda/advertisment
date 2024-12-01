from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user.models import AdUser


class SignUpSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=8)

    class Meta:
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = AdUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class SignInSerializer(ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        user = authenticate(email = data['email'], password = data['password'])
        if not user:
            raise serializers.ValidationError('Invalid User or Password')
        return {"user": user}



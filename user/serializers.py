from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from user.models import AdUser


class SignUpSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=8)

    class Meta:
        model = AdUser
        fields = ('email', 'password')

    def create(self, validated_data):
        user = AdUser.objects.create_user(
            email=validated_data['email'],
            username = validated_data['email'] if validated_data['email'] else validated_data['username'],
            password=validated_data['password']
        )
        # user.save()
        return user

class SignInSerializer(ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AdUser
        fields = ('email', 'password')

    def validate(self, data):
        user = authenticate(email = data['email'], password = data['password'])
        if not user:
            raise ValidationError({'failure': 'Invalid email or password'})
        self.user = user
        return user



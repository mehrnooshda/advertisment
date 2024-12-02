from rest_framework import serializers

from adsmanagement.models import Ad


class AdSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Ad
        fields = ['title', 'owner']
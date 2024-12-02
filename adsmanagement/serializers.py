from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from adsmanagement.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'ad', 'comment_owner']

    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            owner = request.user
        else:
            raise ValidationError("Authentication credentials were not provided.")

        ad = attrs.get('ad')
        if Comment.objects.filter(ad=ad, owner=owner).exists():
            raise ValidationError("You have already commented on this Ad.")

        return attrs


class AdSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'title', 'owner', 'description', 'comments']

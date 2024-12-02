from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from adsmanagement.models import Ad, Comment
from adsmanagement.serializers import AdSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().prefetch_related('comments').order_by('-created_at')
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def list_comments_for_ad(self, request, ad_id=None):
        """
        Retrieve comments for a specific Ad
        """
        if ad_id is None:
            return Response({"error": "Ad ID is required."}, status=400)
        comments = self.queryset.filter(ad_id=ad_id)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
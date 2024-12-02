from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated

from adsmanagement.models import Ad
from adsmanagement.serializers import AdSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

from os.path import basename
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('ads/<int:ad_id>/comments/', CommentViewSet.as_view({'get': 'list_comments_for_ad'}), name='ad-comments'),
]
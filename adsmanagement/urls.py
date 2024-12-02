from os.path import basename

from rest_framework.routers import DefaultRouter
from .views import AdViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = router.urls
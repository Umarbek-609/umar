from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register(r'review', ReviewViewSet, basename='review')

urlpatterns=router.urls
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet,LessonViewSet


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = router.urls
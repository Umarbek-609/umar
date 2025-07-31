from .views import EnrollView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"enroll",EnrollView,basename='enrolll')

urlpatterns = router.urls

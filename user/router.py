from rest_framework.routers import SimpleRouter,DefaultRouter
user = DefaultRouter()
from .views import RegisterView

user.register(r'auth',RegisterView,basename='auth')

urlpatterns = user.urls
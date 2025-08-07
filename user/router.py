from rest_framework.routers import DefaultRouter
user = DefaultRouter()
from .views import RegisterView,ProfileViewSet,RequestPasswordReset,ResetPassword

user.register(r'register',RegisterView,basename='register')
user.register(r'profile',ProfileViewSet,basename='profile')
user.register(r'forgot',RequestPasswordReset,basename='forgot')
user.register(r'repassword',ResetPassword,basename='repassword')


urlpatterns = user.urls
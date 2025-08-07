from rest_framework.routers import DefaultRouter
from django.urls import path
user = DefaultRouter()
from .views import RegisterView,ProfileViewSet,ResetPassword

user.register(r'register',RegisterView,basename='register')
user.register(r'profile',ProfileViewSet,basename='profile')



urlpatterns = user.urls
urlpatterns += [  
    path('reset-password/', ResetPassword.as_view(), name='reset-password'),
]

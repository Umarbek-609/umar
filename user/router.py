from rest_framework.routers import DefaultRouter
from django.urls import path

user = DefaultRouter()
from .views import RegisterView,ProfileViewSet,ResetPassword,PasswordForgetRequestView,PasswordForgetConfirmView

user.register(r'register',RegisterView,basename='register')
user.register(r'profile',ProfileViewSet,basename='profile')

urlpatterns = user.urls
urlpatterns += [  
    path('reset-password/', ResetPassword.as_view(), name='reset-password'),
    path('api/password-reset/', PasswordForgetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordForgetConfirmView.as_view(), name='password-reset-confirm'),
]

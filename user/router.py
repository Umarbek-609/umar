from rest_framework.routers import DefaultRouter
from django.urls import path
user = DefaultRouter()
from .views import RegisterView,ProfileViewSet,RequestPasswordReset,ResetPassword,PasswordResetRequestView,PasswordResetConfirmView

user.register(r'register',RegisterView,basename='register')
user.register(r'profile',ProfileViewSet,basename='profile')



urlpatterns = user.urls
urlpatterns += [  
    path('request-reset-password/', RequestPasswordReset.as_view(), name='request-reset-password'),
    path('reset-password/<uidb64>/<token>/', ResetPassword.as_view(), name='reset-password'),
    path('api/password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),


]

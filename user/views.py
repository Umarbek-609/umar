from .serializer import RegisterSerializer,ProfileSerializer,ResetPasswordSerializer
from rest_framework.response import Response
from .models import CustomUser
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.models import CustomUser,PasswordReset
from rest_framework import status
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import os

class RegisterView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    
class ProfileViewSet(ModelViewSet):
    
    def list(self, request, *args, **kwargs):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data = request.data, instance = request.user, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user":"updated"})
    

class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        new_password = data['new_password']
        confirm_password = data['confirm_password']
        
        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)
        
        reset_obj = PasswordReset.objects.filter().first()
        
        if not reset_obj:
            return Response({'error':'Invalid token'}, status=400)
        
        user = CustomUser.objects.filter(email=reset_obj.email).first()
        
        if user:
            user.set_password(request.data['new_password'])
            user.save()
            
            reset_obj.delete()
            
            return Response({'success':'Password updated'})
        else: 
            return Response({'error':'No user found'}, status=404)

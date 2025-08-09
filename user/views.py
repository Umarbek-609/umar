from .serializer import RegisterSerializer,ProfileSerializer,ResetPasswordSerializer
from .models import CustomUser
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializer import PasswordResetRequestSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings

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

        user = CustomUser.objects.filter(email=request.data['email']).first()

        if user:
            user.set_password(request.data['new_password'])
            user.save()
        
            
            return Response({'success':'Password updated'})
        else: 
            return Response({'error':'No user found'}, status=404)

class PasswordForgetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = CustomUser.objects.get(email=email)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_link = request.build_absolute_uri(f"/auth/password-reset-confirm/{uid}/{token}/")
                # Send email
                send_mail(
                    subject="Reset your password",
                    message=f"Click the link to reset your password: {reset_link}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                )

                return Response({"message": "Password reset link sent."}, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordForgetConfirmView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (CustomUser.DoesNotExist, ValueError, TypeError, OverflowError):
            return Response({'error': 'Noto‘g‘ri token yoki foydalanuvchi.'}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            new_password = request.data.get("new_password")
            if not new_password:
                return Response({'error': 'Yangi parol kiritilmadi.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({'message': 'Parol muvaffaqiyatli yangilandi.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Token yaroqsiz yoki eskirgan.'}, status=status.HTTP_400_BAD_REQUEST)





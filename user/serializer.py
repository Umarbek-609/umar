from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework import serializers
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings 
import re

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField()  

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1',"password2",'user_type')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("parollar bir biriga mos kemadi.")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1'],
            user_type=validated_data['user_type'],
        )
        send_mail(
            message ="bemalol saitdan foydalaning",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list = [user.email],
            fail_silently=False,
        )

        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        write_only=True,
        error_messages={'invalid': ('Password must be at least 8 characters long with at least one capital letter and symbol')}
    )
    confirm_password = serializers.CharField(write_only=True, required=True)



class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$', value):
            raise serializers.ValidationError(
                "Parol kamida 8 ta belgidan iborat, katta harf, raqam va maxsus belgi bo'lishi kerak.")
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Parollar mos emas")
        return data

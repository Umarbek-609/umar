from rest_framework import serializers
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings 


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1',"password2")

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("parollar bir biriga mos kemadi.")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1'],
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

class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        write_only=True,
        error_messages={'invalid': ('Password must be at least 8 characters long with at least one capital letter and symbol')}
    )
    confirm_password = serializers.CharField(write_only=True, required=True)
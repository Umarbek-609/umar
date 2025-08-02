from django.shortcuts import render
from .serializer import RegisterSerializer
from .models import CustomUser
from rest_framework.viewsets import ViewSet

class RegisterView(ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    
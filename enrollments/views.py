from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import EnrollSerializer
from .models import Enroll
from rest_framework.permissions import IsAuthenticated

class EnrollView(ModelViewSet):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer
    permission_classes = [IsAuthenticated()]
    

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Enroll.objects.all()
        return Enroll.objects.filter(user=user)
    
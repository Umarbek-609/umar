from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .serializer import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    pass



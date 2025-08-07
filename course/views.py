from rest_framework import viewsets, permissions, filters
from .models import Course,Lessons
from .serializer import CourseSerializer,LessonSerializer
from utils.permissions import IsOwnerOrReadOnly,IsCourseOwnerOrReadOnly
from utils.pagination import CustomPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsCourseOwnerOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
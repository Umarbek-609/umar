from rest_framework import viewsets, permissions, filters
from .models import Course
from .serializer import CourseSerializer
from utils.permissions import IsOwnerOrReadOnly
from utils.pagination import CustomPagination


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = [CustomPagination]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)
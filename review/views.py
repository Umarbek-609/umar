from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializer import ReviewSerializer
from utils.permissions import IsStudent


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsStudent]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.all(is_visible=True)
    
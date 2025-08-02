from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializer import ReviewSerializer
from utils.permissions import IsRegistered

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsRegistered]

    def get_queryset(self):
        return Review.objects.all(user=self.request.user)
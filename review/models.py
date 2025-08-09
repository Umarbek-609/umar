from django.db import models
from course.models import Course

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    user = models.ForeignKey('user.Student', on_delete=models.CASCADE)
    text = models.CharField(verbose_name="review",max_length=200)
    rayting = models.IntegerField(verbose_name="rayting")
    is_visible = models.BooleanField(default=True) 
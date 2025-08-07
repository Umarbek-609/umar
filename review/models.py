from django.db import models
from course.models import Course

class Review(models.Model):
    coure = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    first_name = models.CharField(verbose_name="Familiya",max_length=200,blank=True,null=True)
    last_name = models.CharField(verbose_name="Ism",max_length=200,blank=True,null=True)
    text = models.CharField(verbose_name="review",max_length=200)
    rayting = models.IntegerField(verbose_name="rayting")

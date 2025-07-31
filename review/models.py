from django.db import models

class Review(models.Model):
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    text = models.CharField(max_length=200)
    rayting = models.IntegerField()

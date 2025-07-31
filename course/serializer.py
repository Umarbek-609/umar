from rest_framework import serializers
from .models import Course,Lessons

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'

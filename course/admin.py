from django.contrib import admin
from .models import Course,Lessons

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']



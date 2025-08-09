from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Course,Lessons

@admin.register(Course)
class CategoryAdmin(TranslatableAdmin):  
    list_display = ['title','description']

@admin.register(Lessons)
class CategoryAdmin(TranslatableAdmin):  
    list_display = ['title']



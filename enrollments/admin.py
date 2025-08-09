# enroll/admin.py
from django.contrib import admin
from .models import Enroll

@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ['user','course','progress','completed','has_certificate']

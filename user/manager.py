from django.contrib.auth.models import BaseUserManager

class TeacherManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='teacher')
    
class StudentrManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='student')
from django.contrib.auth.models import BaseUserManager

class InstructorManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='instructor')
    
class StudentManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='student')
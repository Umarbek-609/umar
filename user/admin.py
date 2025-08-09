from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Instructor,Student

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Qo‘shimcha ma’lumotlar', {'fields': ('phone_number',)}),
    )

admin.site.register(Instructor)
admin.site.register(Student)

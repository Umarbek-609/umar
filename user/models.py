from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .manager import InstructorManager,StudentManager
from utils.models import ModelWithTimeStemp

class CustomUser(AbstractUser,ModelWithTimeStemp):
    class UserTypeEnum(models.TextChoices):
        INSTRUCTOR = 'instructor', _('Instructor')
        STUDENT = 'student', _('Student')
    user_type = models.CharField(verbose_name=_("user_type"),max_length=100,choices=UserTypeEnum.choices,
                                default=UserTypeEnum.STUDENT,blank=True)
    email_verified = models.BooleanField(verbose_name=_("email_verified"),default=False)

    @property
    def verify_email(self):
        self.email_verified = True
        self.save()


class Instructor(CustomUser):
    objects = InstructorManager()

    class Meta:
        proxy = True
        verbose_name=_("Instructor")

class Student(CustomUser):
    objects = StudentManager ()

    class Meta:
        proxy = True
        verbose_name=_("Student")


class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
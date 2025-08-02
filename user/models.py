from django.db import models
from utils.models import ModelWithTimeStamp
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .manager import TeacherManager,StudentrManager

class CustomUser(AbstractUser):
    class UserTypeEnum(models.TextChoices):
        TEACHER = 'teacher', _('Teacher')
        STUDENT = 'student', _('Student')
    user_type = models.CharField(verbose_name=_("user_type"),max_length=100,choices=UserTypeEnum.choices,
                                default=UserTypeEnum.STUDENT,blank=True)

    @property
    def verify_email(self):
        self.email_verified = True
        self.save()


class Applicant(CustomUser):
    objects = TeacherManager()

    class Meta:
        proxy = True
        verbose_name=_("Teacher")

class Employer(CustomUser):
    objects = StudentrManager ()

    class Meta:
        proxy = True
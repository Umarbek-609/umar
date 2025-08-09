from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import CustomUser
from course.models import Course

class Enroll(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_('Student'))
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=_('Course'))
    enrolled_at = models.DateTimeField(verbose_name=_("shu vaqt"),auto_now_add=True)
    last_accessed = models.DateTimeField(verbose_name=_("last_accessed"),auto_now=True)
    progress = models.IntegerField(verbose_name=_("progress"),default=0)
    completed = models.BooleanField(verbose_name=_("completed"),default=False)
    has_certificate = models.BooleanField(verbose_name=_('has_certificate'),default=False)
    is_active = models.BooleanField(verbose_name=_('is_active'),default=False)
    

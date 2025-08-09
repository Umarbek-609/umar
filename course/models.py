from django.db import models
from parler.models import TranslatableModel,TranslatedFields
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _

class Course(TranslatableModel):

    class Meta:
        verbose_name = "Course"
        ordering = ['-created_at']

    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField(),
    )
    image = models.ImageField(verbose_name=_("image"),upload_to='course_image/',blank=True,null=True)
    price = models.FloatField(verbose_name=_("price"),default=0)
    instructor = models.ForeignKey('user.Instructor',on_delete=models.CASCADE,verbose_name=_("instructor"))
    created_at = models.DateTimeField(verbose_name=_("created_at"),auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("updated_at"),auto_now=True)
    average_rating = models.FloatField(verbose_name=_("average_rating"),default=0)

    def __str__(self):
        return self.safe_translation_getter('title',any_language=True)
    
    def update_rating(self):

        avg = self.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
        self.average_rating = round(avg, 1)
        self.save(update_fields=['average_rating'])


class Lessons(TranslatableModel):
    
    class Meta:
        verbose_name = "Lesson"
        ordering = ['order']

    translations = TranslatedFields(
        title = models.CharField(max_length=200)
    )

    video_link = models.URLField(verbose_name=_("video_link"))
    order = models.IntegerField(verbose_name=_("order"))
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name=_("course"))
    
    def __str__(self):
        return self.safe_translation_getter('title',any_language=True)
from django.db import models
from parler.models import TranslatableModel,TranslatedFields
from django.db.models import Avg

class Course(TranslatableModel):

    class Meta:
        verbose_name = "Course"
        ordering = ['-created_at']

    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField(),
    )
    image = models.ImageField(upload_to='course_image/')
    price = models.FloatField()
    instructor = models.ForeignKey('user.Instructor',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.safe_translation_getter('title',any_language=True) or "none"
    
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

    video_link = models.URLField()
    order = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.safe_translation_getter('title',any_language=True)
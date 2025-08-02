from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Course, Lessons

class CourseSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Course)
    class Meta:
        model = Course
        fields = ['id', 'translations', 'image', 'price', 'instructor', 'created_at', 'updated_at']


class LessonSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Lessons)
    class Meta:
        model = Lessons
        fields = ['id', 'translations', 'video_link', 'order', 'course']

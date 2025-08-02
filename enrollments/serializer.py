from rest_framework import serializers
from .models import Enroll
from parler_rest.serializers import TranslatableModelSerializer,TranslatedFieldsField

class EnrollSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Enroll)

    class Meta:
        model = Enroll
        fields = '__all__'



    def validate(self,data):
        user = self.context['request'].user
        course = data['course']
        if Enroll.objects.filter(user=user,course=course).exists():
            raise serializers.ValidationError("bu kursga ro'yxatdan o'tbogansan jinni")
        return data
    
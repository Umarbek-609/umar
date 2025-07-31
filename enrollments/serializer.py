from rest_framework import serializers
from .models import Enroll

class EnrollSerializer(serializers.ModelSerializer):
    model = Enroll
    fields = '__all__'

    def validate(self,data):
        user = self.context['request'].user
        course = data['course']
        if Enroll.objects.filter(user=user,course=course).exists():
            raise serializers.ValidationError("bu kursga ro'yxatdan o'tbogansan jinni")
        return data
    
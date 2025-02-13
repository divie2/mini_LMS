from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *


class CreateCourseSerializer(serializers.ModelSerializer):
    """Serializer for Course creation """

    class Meta :
        model = Course
        fields = ['id','title','description', 'price']
        read_only_fields = ['id']


class ListCoursesSerializer(serializers.ModelSerializer):
    """Serializer for listing courses"""

    class Meta :
        model = Course
        fields = ['id','title','description', 'price']
        read_only_fields = ['id']


class UpdateCourseSerializer(serializers.ModelSerializer):
    """Serializer for updating courses"""

    class Meta :
        model = Course
        fields = ['id','title','description', 'price']
        read_only_fields = ['id']

    def update(self,instance, validated_data):

        if 'title' in validated_data:
            title_id = validated_data.pop('title', None)

            instance.title = title_id

        if 'description' in validated_data:
            description_id = validated_data.pop('description', None)

            instance.description = description_id

        if 'price' in validated_data:
            price_id = validated_data.pop('price', None)

            instance.price = price_id

        instance = super().update(instance, validated_data)

        return instance

class EnrollmentSerializer(serializers.ModelSerializer):

        user = models.CharField()
        course = models.CharField()

        class Meta:
            model = Enrollment
            fields = ['id','user', 'course']
            read_only_fields = ['id','user']

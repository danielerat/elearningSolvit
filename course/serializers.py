from rest_framework import serializers
from .models import Course, Module, Lesson, Content
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'duration', 'instructor']


class ModuleSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Module
        fields = ['id', 'title', 'description', 'course', 'order']


class LessonSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'module', 'order']


class ContentSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = Content
        fields = ['id', 'lesson', 'order', 'content_type', 'title', 'text', 'video_url', 'document_file', 'activity_url']

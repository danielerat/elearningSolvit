from rest_framework import serializers
from .models import Course, Module, Lesson, Content
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
# Simplified serializers for the Module
class SimpleLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields=["title"]
# Simplified serializers for courses
class SimpleModuleSerializer(serializers.ModelSerializer):
    lesson_set=SimpleLessonSerializer(many=True,read_only=True)
    class Meta:
        model = Module
        fields = ['title','lesson_set']
class SimpleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id','content_type', 'title']

class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)
    module_set=SimpleModuleSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'duration', 'instructor','module_set']

    def create(self, validated_data):
        instructor_id=self.context['instructor_id']
        return Course.objects.create(instructor_id=instructor_id,**validated_data)


class ModuleSerializer(serializers.ModelSerializer):
    
    lesson_set=SimpleLessonSerializer(many=True,read_only=True)
    class Meta:
        model = Module
        fields = ['id', 'title', 'description', 'order',"lesson_set"]
    def create(self, validated_data):
        course_id=self.context['course_id']
        return Module.objects.create(course_id=course_id,**validated_data)


class LessonSerializer(serializers.ModelSerializer):
    content_set=SimpleContentSerializer(many=True,read_only=True)
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'order','content_set']
    def create(self, validated_data):
        module_id=self.context['module_id']
        return Lesson.objects.create(module_id=module_id,**validated_data)


class ContentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Content
        fields = ['id',  'order', 'content_type', 'title', 'text', 'video_url', 'document_file', 'activity_url']
    
    def create(self, validated_data):
        lesson_id=self.context['lesson_id']
        return Content.objects.create(lesson_id=lesson_id,**validated_data)


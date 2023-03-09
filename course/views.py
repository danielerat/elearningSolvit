from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Module, Lesson, Content
from .serializers import CourseSerializer, ModuleSerializer, LessonSerializer, ContentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from course.filters import CourseFilter
class IsInstructorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow instructors to edit their courses.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the instructor of the course.
        return obj.instructor == request.user


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_class=CourseFilter
    search_fields=['title','description','instructor__first_name','instructor__last_name']
    def get_serializer_context(self):
        return {'instructor_id':1}
    
class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    # permission_classes = [IsInstructorOrReadOnly]
    def get_queryset(self):
        return Module.objects.filter(course_id=self.kwargs['course_pk'])
    def get_serializer_context(self):
        return {'course_id':self.kwargs['course_pk']}

class LessonViewSet(viewsets.ModelViewSet):
    
    serializer_class = LessonSerializer
    def get_queryset(self):
        return Lesson.objects.filter(module_id=self.kwargs['module_pk'])
    
    def get_serializer_context(self):
        return {'module_id':self.kwargs['module_pk']}
    # permission_classes = [IsInstructorOrReadOnly]

    

class ContentViewSet(viewsets.ModelViewSet):
    
    serializer_class = ContentSerializer
    def get_queryset(self):
        return Content.objects.filter(lesson_id=self.kwargs['lesson_pk'])
    # permission_classes = [IsInstructorOrReadOnly]
    def get_serializer_context(self):
        return {'lesson_id':self.kwargs['lesson_pk']}
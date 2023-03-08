from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Module, Lesson, Content
from .serializers import CourseSerializer, ModuleSerializer, LessonSerializer, ContentSerializer


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
    # permission_classes = [IsInstructorOrReadOnly]

    @action(detail=True, methods=['get'])
    def modules(self, request, pk=None):
        course = self.get_object()
        modules = course.module_set.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsInstructorOrReadOnly]

    @action(detail=True, methods=['get'])
    def lessons(self, request, pk=None):
        module = self.get_object()
        lessons = module.lesson_set.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsInstructorOrReadOnly]

    @action(detail=True, methods=['get'])
    def contents(self, request, pk=None):
        lesson = self.get_object()
        contents = lesson.content_set.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    # permission_classes = [IsInstructorOrReadOnly]

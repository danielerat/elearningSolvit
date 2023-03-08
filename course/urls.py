from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import CourseViewSet, ModuleViewSet, LessonViewSet, ContentViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'courses', CourseViewSet)

# Nested router for module viewsets
module_router = routers.NestedDefaultRouter(router, r'courses', lookup='course')
module_router.register(r'modules', ModuleViewSet, basename='module')

# Nested router for lesson viewsets
lesson_router = routers.NestedDefaultRouter(module_router, r'modules', lookup='module')
lesson_router.register(r'lessons', LessonViewSet, basename='lesson')

# Nested router for content viewsets
content_router = routers.NestedDefaultRouter(lesson_router, r'lessons', lookup='lesson')
content_router.register(r'content', ContentViewSet, basename='content')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(module_router.urls)),
    path('', include(lesson_router.urls)),
    path('', include(content_router.urls)),
]

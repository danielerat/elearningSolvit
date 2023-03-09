from django.contrib import admin
from .models import Course, Module, Lesson, Content

# Define the admin classes for each model
class ModuleInline(admin.StackedInline):
    model = Module
    extra = 0

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0

class ContentInline(admin.StackedInline):
    model = Content
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]

class ModuleAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('id','title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title', 'description')

class LessonAdmin(admin.ModelAdmin):
    inlines = [ContentInline]
    list_display = ('title', 'module', 'order')
    list_filter = ('module__course', 'module')
    search_fields = ('title', 'description')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'order', 'content_type')
    list_filter = ('lesson__module__course', 'lesson__module', 'lesson')
    search_fields = ('title', 'text')

# Register the admin classes for each model
admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Content, ContentAdmin)

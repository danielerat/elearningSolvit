
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200) # The title of the course.
    description = models.TextField(blank=True, null=True) # A description of the course.
    duration = models.PositiveIntegerField(blank=True, null=True) # The duration of the course in hours.
    instructor = models.ForeignKey(User, on_delete=models.CASCADE) # The instructor who is teaching the course.

    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=200) # The title of the module.
    description = models.TextField(blank=True, null=True) # A description of the module.
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # The course that this module belongs to.
    order = models.PositiveIntegerField() # The order in which this module appears within the course.

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'

class Lesson(models.Model):
    title = models.CharField(max_length=200) # The title of the lesson.
    description = models.TextField(blank=True, null=True) # A description of the lesson.
    module = models.ForeignKey(Module, on_delete=models.CASCADE) # The module that this lesson belongs to.
    order = models.PositiveIntegerField() # The order in which this lesson appears within the module.

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'

class Content(models.Model):
    CONTENT_TYPES = (
        ('text', 'Text'), # A text-based content type.
        ('video', 'Video'), # A video-based content type.
        ('document', 'Document'), # A document-based content type.
        ('activity', 'Activity') # An interactive activity-based content type.
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE) # The lesson that this content belongs to.
    order = models.PositiveIntegerField() # The order in which this content appears within the lesson.
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPES) # The type of content (text, video, document, or activity).
    title = models.CharField(max_length=200) # The title of the content.
    text = models.TextField(blank=True, null=True) # The text content, if this is a text-based content type.
    video_url = models.URLField(blank=True, null=True) # The URL of the video content, if this is a video-based content type.
    document_file = models.FileField(upload_to='documents/', blank=True, null=True) # The uploaded document file, if this is a document-based content type.
    activity_url = models.URLField(blank=True, null=True) # The URL of the interactive activity, if this is an activity-based content type.

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'

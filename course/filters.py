from django_filters.rest_framework import FilterSet

from course.models import Course

class CourseFilter(FilterSet):
    class Meta:
        model=Course
        fields={
            'instructor__first_name':['exact'],
            'duration':['gt','lt']
            }
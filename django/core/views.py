from django.views.generic import ListView

from core.models import Classroom, Course, Subject


class ClassroomListView(ListView):
    model = Classroom
    template_name = 'list/classrom_list.html'


class CourseListView(ListView):
    model = Course
    template_name = 'list/course_list.html'


class SubjectListView(ListView):
    model = Subject
    template_name = 'list/subject_list.html'

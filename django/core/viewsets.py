from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from core.models import Classroom, Course, Subject
from core.serializers import ClassroomSerializer, CourseSerializer, SubjectSerializer
from core.tasks import import_classrooms, import_courses, import_subjects
from core.utils import save_to_import


class ClassroomViewSet(viewsets.ModelViewSet):

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file_path = save_to_import(request.FILES['file'])
        import_classrooms(file_path)
        return Response({'a': 'b'})


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file_path = save_to_import(request.FILES['file'])
        import_courses(file_path)
        return Response({'a': 'b'})


class SubjectViewSet(viewsets.ModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file_path = save_to_import(request.FILES['file'])
        import_subjects(file_path)
        return Response({'a': 'b'})

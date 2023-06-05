from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from questions.models import Question
from questions.serializers import QuestionSerializer
from questions.tasks import import_questions
from core.utils import save_to_import


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file_path = save_to_import(self.request.FILES['file'])
        import_questions(file_path)
        return Response({'message': 'Success'})

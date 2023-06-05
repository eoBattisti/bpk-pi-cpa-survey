from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import User
from users.serializers import UserSerializer
from users.tasks import import_users
from core.utils import save_to_import


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file_path = save_to_import(self.request.FILES['file'])
        import_users(file_path)
        return Response({'message': 'Success'})

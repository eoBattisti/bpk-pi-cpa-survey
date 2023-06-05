from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from axis.models import Axle
from axis.serializers import AxleSerializer
from axis.tasks import import_axles
from core.utils import save_to_import


class AxleViewSet(viewsets.ModelViewSet):

    queryset = Axle.objects.all()
    serializer_class = AxleSerializer

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file_path = save_to_import(request.FILES['file'])
        import_axles(file_path)
        return Response({'message': 'Success'})

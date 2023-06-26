from rest_framework import viewsets

from axis.models import Axle

from axis.serializers import AxleSerializer


class AxleViewSet(viewsets.ModelViewSet):

    queryset = Axle.objects.all()
    serializer_class = AxleSerializer
    
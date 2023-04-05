from rest_framework import serializers

from axis.models import Axle

class AxleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Axle
        fields = '__all__'
        datatables_always_serialize = ('id',)
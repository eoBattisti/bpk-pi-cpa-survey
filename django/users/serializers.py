from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name

    class Meta:
        model = User
        fields = ['name', 'ra', 'role', 'cpa_member', 'email']
        datatables_always_serialize = ('id',)

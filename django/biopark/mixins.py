"""list of mixins of aplication"""


class ListViewSerializerMixin:
    """ set the serializer to the listing"""
    def get_serializer_class(self):
        """Get the class to serializer"""
        serializer = super().get_serializer_class()
        if self.action == 'list':
            serializer = self.list_serializer
        return serializer

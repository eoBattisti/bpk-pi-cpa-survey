import factory

from axis.models import Axle

class AxleFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('sentence', nb_words=1, locale='pt_BR')
    description = factory.Faker('sentence', nb_words=5, locale='pt_BR')

    class Meta:
        model = Axle
        django_get_or_create = ('name',)

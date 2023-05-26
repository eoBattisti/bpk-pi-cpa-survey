import factory
from factory.fuzzy import FuzzyChoice
from core import defaults
from users.models import Area, AreaEmployee, User


class UserFactory(factory.django.DjangoModelFactory):

    first_name = factory.Faker('first_name', locale='pt_BR')
    last_name = factory.Faker('last_name', locale='pt_BR')
    email = factory.Sequence(lambda n: f'user-{n}@biopark.com')
    password = factory.PostGenerationMethodCall('set_password', 'atena')

    cpf = factory.Sequence(lambda n: '%11d' % n)  # pylint: disable=consider-using-f-string
    ra = factory.Sequence(lambda n: '000%02d' % n)  # pylint: disable=consider-using-f-string,invalid-name
    role = FuzzyChoice([id[0] for id in defaults.USER_ROLES])
    cpa_member = FuzzyChoice([True, False])

    class Meta:
        model = User
        django_get_or_create = ('cpf',)


class AreaFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=1, locale='pt_BR')

    class Meta:
        model = Area
        django_get_or_create = ('name',)


class AreaEmployeeFactory(factory.django.DjangoModelFactory):
    area = factory.SubFactory(Area)
    employee = factory.SubFactory(UserFactory)

    class Meta:
        model = AreaEmployee
        django_get_or_create = ('area', 'employee',)

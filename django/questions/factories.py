import factory
from factory.fuzzy import FuzzyChoice

from core import defaults
from axis.factories import AxleFactory
from questions.models import Question


class QuestionFactory(factory.django.DjangoModelFactory):

    axis = factory.SubFactory(AxleFactory)
    answer_type = FuzzyChoice([id[0] for id in defaults.ANSWER_TYPES])
    description = factory.Faker('sentence', nb_words=5, locale='pt_BR')

    class Meta:
        model = Question
        django_get_or_create = ('axis', 'description',)

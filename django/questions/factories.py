import random

import factory

from core import defaults
from axis.factories import AxleFactory
from questions.models import Question


class QuestionFactory(factory.django.DjangoModelFactory):

    axis = factory.SubFactory(AxleFactory)
    answer_type = random.choice(defaults.ANSWER_TYPES)[0]
    description = factory.Faker('sentence', nb_words=5, locale='pt_BR')

    class Meta:
        model = Question
        django_get_or_create = ('axis', 'description',)

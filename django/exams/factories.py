import random
import factory

from core.factories import SubjectFactory
from exams.models import Exam, ExamQuestion, Answer
from questions.factories import QuestionFactory
from users.factories import AreaFactory, UserFactory


class ExamFactory(factory.django.DjangoModelFactory):

    title = factory.Faker('sentence', nb_words=3, locale='pt_BR')
    start_date = factory.Faker('date_this_year')
    end_date = factory.Faker('date_this_year')
    responsible = factory.SubFactory(UserFactory)
    area = factory.SubFactory(AreaFactory)
    subject = factory.SubFactory(SubjectFactory)

    class Meta:
        model = Exam
        django_get_or_create = ('title',)


class ExamQuestionFactory(factory.django.DjangoModelFactory):
    exam = factory.SubFactory(ExamFactory)
    question = factory.SubFactory(QuestionFactory)

    class Meta:
        model = ExamQuestion
        django_get_or_create = ('exam', 'question',)


class AnswersFactory(factory.django.DjangoModelFactory):
    description = factory.Faker('sentence', nb_words=10, locale='pt_BR')
    value = random.randint(1, 10)
    exam_question = factory.SubFactory(ExamQuestionFactory)
    answerd_by = factory.SubFactory(UserFactory)

    class Meta:
        model = Answer
        django_get_or_create = ('answerd_by',)

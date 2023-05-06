import logging
from django.core.management import BaseCommand

from core.management.commands.builders import areas, axis, exams, questions, users

LOGGER = logging.getLogger('django')


class Command(BaseCommand):
    cache = {}
    size = 5

    def print(self, text):
        LOGGER.info('[BUILD DATABASE] %s', text)

    def handle(self, *args, **options):
        self.print('Populating database...')

        users.create_coordenators(self)
        users.create_teachers(self)
        users.create_employees(self)
        users.create_students(self)

        # areas.create_areas(self)

        areas.create_areas_employees(self)
        areas.create_courses(self)
        areas.create_classroom(self)
        areas.create_subjects(self)
        areas.create_classroom_students(self)

        axis.create(self)

        questions.create_questions(self)

        exams.create_exams(self)
        exams.create_exams_questions(self)
        exams.create_answers(self)

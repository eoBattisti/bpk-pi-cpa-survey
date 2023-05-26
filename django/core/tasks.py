""" Axle's module tasks."""

import logging
from datetime import datetime
import pandas as pd
from pandas.errors import EmptyDataError

from django.core.files.storage import default_storage
from django.db import IntegrityError, transaction
from django.db.models import Value
from django.db.models.functions import Concat

from core import defaults
from core.models import Classroom, Course
from users.models import User

LOGGER = logging.getLogger('django')


def import_classrooms(file_path):

    try:
        file_data = default_storage.open(file_path, 'rb')
        xls = pd.read_csv(file_data)

        with transaction.atomic():
            for row in xls.itertuples(index=False):
                course = Course.objects.filter(title=row[3]).first()
                Classroom.objects.update_or_create(title=str(row[0]),
                                                   start_date=datetime.strptime(
                                                       row[1],
                                                       defaults.STRING_DATETIME_FORMAT),
                                                   end_date=datetime.strptime(
                                                       row[2],
                                                       defaults.STRING_DATETIME_FORMAT),
                                                   course=course)
    except IntegrityError:
        LOGGER.info('Erro de integridade. Por favor verifique os campos do arquivo!')
    except EmptyDataError:
        LOGGER.info('Erro no arquivo. Por favor valide se o arquivo possui todos os campos preenchidos')
    except Exception:  # pylint: disable=broad-except
        LOGGER.info('Erro inesperado! Por favor entre em contato com o suporte')


def import_courses(file_path):

    try:
        file_data = default_storage.open(file_path, 'rb')
        xls = pd.read_csv(file_data)

        with transaction.atomic():
            for row in xls.itertuples(index=False):
                users = User.objects.filter(role__in=[defaults.USER_ROLE_CORDENATOR,
                                                      defaults.USER_ROLE_TEACHER])
                users = users.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
                coordenator = users.filter(full__name__icontains=row[2]).first()

                if coordenator.role != defaults.USER_ROLE_CORDENATOR:
                    coordenator.role = defaults.USER_ROLE_CORDENATOR
                    coordenator.save()

                Course.objects.update_or_create(title=str(row[0]),
                                                alias=str(row[1]),
                                                coordenator=coordenator)
    except IntegrityError:
        LOGGER.info('Erro de integridade. Por favor verifique os campos do arquivo!')
    except EmptyDataError:
        LOGGER.info('Erro no arquivo. Por favor valide se o arquivo possui todos os campos preenchidos')
    except Exception:  # pylint: disable=broad-except
        LOGGER.info('Erro inesperado! Por favor entre em contato com o suporte')


def import_subjects(file_path):

    try:
        file_data = default_storage.open(file_path, 'rb')
        xls = pd.read_csv(file_data)

        with transaction.atomic():
            for row in xls.itertuples(index=False):
                users = User.objects.filter(role__in=[defaults.USER_ROLE_CORDENATOR,
                                                      defaults.USER_ROLE_TEACHER])
                users = users.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
                teacher = users.filter(full__name__icontains=row[2]).first()
                Course.objects.update_or_create(title=str(row[0]),
                                                course=str(row[1]),
                                                teacher=teacher)
    except IntegrityError:
        LOGGER.info('Erro de integridade. Por favor verifique os campos do arquivo!')
    except EmptyDataError:
        LOGGER.info('Erro no arquivo. Por favor valide se o arquivo possui todos os campos preenchidos')
    except Exception:  # pylint: disable=broad-except
        LOGGER.info('Erro inesperado! Por favor entre em contato com o suporte')

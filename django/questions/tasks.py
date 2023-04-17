""" Axle's module tasks."""
import logging
import pandas as pd
from pandas.errors import EmptyDataError

from django.core.files.storage import default_storage
from django.db import IntegrityError, transaction

from axis.models import Axle
from core import defaults
from questions.models import Question


LOGGER = logging.getLogger('django')


def import_questions(file_path):

    try:
        file_data = default_storage.open(file_path, 'rb')
        xls = pd.read_csv(file_data)

        with transaction.atomic():
            for row in xls.itertuples(index=False):
                axle = Axle.objects.filter(name__contains=row[1])
                Question.objects.update_or_create(description=str(row[0]),
                                                  axis=axle,
                                                  answer_type=defaults.ANSWER_TYPES[row[2]])
    except IntegrityError:
        LOGGER.info('Erro de integridade. Por favor verifique os campos do arquivo!')
    except EmptyDataError:
        LOGGER.info('Erro no arquivo. Por favor valide se o arquivo possui todos os campos preenchidos')
    except Exception:  # pylint: disable=broad-except
        LOGGER.info('Erro inesperado! Por favor entre em contato com o suporte')

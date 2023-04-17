""" Axle's module tasks."""
import logging
import pandas as pd
from pandas.errors import EmptyDataError

from django.core.files.storage import default_storage
from django.db import IntegrityError, transaction


from axis.models import Axle

LOGGER = logging.getLogger('django')


def import_axles(file_path):

    try:
        file_data = default_storage.open(file_path, 'rb')
        xls = pd.read_csv(file_data)

        with transaction.atomic():
            for row in xls.itertuples(index=False):
                Axle.objects.update_or_create(name=str(row[0]),
                                              description=str(row[1]))
    except IntegrityError:
        LOGGER.info('Erro de integridade. Por favor verifique os campos do arquivo!')
    except EmptyDataError:
        LOGGER.info('Erro no arquivo. Por favor valide se o arquivo possui todos os campos preenchidos')
    except Exception:  # pylint: disable=broad-except
        LOGGER.info('Erro inesperado! Por favor entre em contato com o suporte')

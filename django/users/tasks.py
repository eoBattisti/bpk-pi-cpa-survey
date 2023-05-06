""" Axle's module tasks."""
import logging
import pandas as pd
from pandas.errors import EmptyDataError, DataError

from django.core.files.storage import default_storage
from django.db import IntegrityError, transaction

from core import defaults
from core.models import Classroom, ClassroomStudent
from users.models import User, Area, AreaEmployee

LOGGER = logging.getLogger('django')


def import_users(file_path):

    try:
        file_data = default_storage.open(file_path, 'rb')
        xls = pd.read_csv(file_data)
        user_roles = {
             "Coordenador": defaults.USER_ROLE_CORDENATOR,
             "Aluno": defaults.USER_ROLE_STUDENT,
             "Professor": defaults.USER_ROLE_TEACHER,
             "Funcionario": defaults.USER_ROLE_EMPLOYEE
        }
        with transaction.atomic():
            for row in xls.itertuples(index=False):  # pylint: disable=unused-variable
                user = User.objects.update_or_create(first_name=row[0],
                                                     last_name=row[1],
                                                     email=row[2],
                                                     cpf=row[4],
                                                     ra=row[5],
                                                     cpa_member=row[6],
                                                     role=user_roles[row[7]])
                # Define a senha do usuário como sendo a data de nascimento dele
                user.set_password(row[3])
                user.save()
                if user_roles[row[7]] == defaults.USER_ROLE_STUDENT:
                    classroom = Classroom.objects.filter(title=row[9]).first()
                    if classroom.DoesNotExist:
                        raise DataError
                    ClassroomStudent.objects.create(classroom=classroom,
                                                    student=user)
                else:
                    area = Area.objects.filter(name=row[8]).first()
                    AreaEmployee.objects.create(area=area,
                                                employee=user)
    except DataError:
        LOGGER.info('Erro no campo classroom: Por favor verifique se todos os valores existem no sistema')
    except IntegrityError:
        LOGGER.info('Erro de integridade. Por favor verifique os campos do arquivo!')
    except EmptyDataError:
        LOGGER.info('Erro no arquivo. Por favor valide se o arquivo possui todos os campos preenchidos')
    except Exception:  # pylint: disable=broad-except
        LOGGER.info('Erro inesperado! Por favor entre em contato com o suporte')

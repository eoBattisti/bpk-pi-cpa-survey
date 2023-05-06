import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core import defaults
from core.models import BaseModel


class User(AbstractUser):
    """
    Model para representar os usuários do sistema.
    Este model herda de AbstractUser pois essa classe
    já contém diversos campos que podem ser utilizados.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    ra = models.CharField(verbose_name="RA", max_length=8)  # pylint: disable=invalid-name
    role = models.SmallIntegerField(verbose_name='Role', choices=defaults.USER_ROLES)
    cpa_member = models.BooleanField(verbose_name="CPA Member", default=False)
    username = models.CharField(max_length=1, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='E-mail de login')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name()


class Area(BaseModel):
    """
    Model para representar as áreas dentro da instituição
    exemplo: financeiro, cantina, etc.
    """
    name = models.CharField(verbose_name=_("Name"), max_length=50)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __str__(self) -> str:
        return self.name


class AreaEmployee(models.Model):

    area = models.ForeignKey("users.Area",
                             verbose_name=_("Area"),
                             related_name="employees",
                             on_delete=models.CASCADE)
    employee = models.ForeignKey("users.User",
                                 verbose_name=_("Employee"),
                                 related_name="area",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("AreaEmployee")
        verbose_name_plural = _("AreaEmployees")

    def __str__(self):
        return f'{self.area} - {self.employee}'

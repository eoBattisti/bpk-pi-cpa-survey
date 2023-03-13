from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

# Create your models here.
class Axle(BaseModel):

    name = models.CharField(verbose_name=_("Name"), max_length=50)
    description = models.TextField(verbose_name=_("Description"), null=True)

    class Meta:
        verbose_name = "Eixo"
        verbose_name_plural = "Eixos"

    def __str__(self):
        return self.name

from django.db import models
from django.utils.translation import gettext_lazy as _

from core import defaults
from core.models import BaseModel
from axis.models import Axle


class Question(BaseModel):

    description = models.TextField(verbose_name=_("Description"))
    axis = models.ForeignKey(Axle,
                             verbose_name=_("Axis"),
                             related_name='questions',
                             on_delete=models.CASCADE)
    answer_type = models.SmallIntegerField(verbose_name=_("Answer type"),
                                           choices=defaults.ANSWER_TYPES,
                                           default=defaults.ANSWER_TYPE_OBJECTIVE)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.description

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Basic model
    """
    created = models.DateTimeField(_('Время создания'), auto_now_add=True)
    updated = models.DateTimeField(_('Время изменения'), auto_now=True)

    class Meta:
        abstract = True

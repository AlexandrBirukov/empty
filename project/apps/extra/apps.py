from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExtraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.apps.extra'
    verbose_name = _('Общие настройки')

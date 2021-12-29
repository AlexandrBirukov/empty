from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from project.utils.models import BaseModel


class CounterQuerySet(models.QuerySet):
    """Extended queryset for Counter model."""

    def approved(self):
        """Return approved counters"""
        return self.filter(is_approved=True)


class Counter(models.Model):
    """
    Модель для вставки дополнительного кода в <header>, после <body> и перед </body>
    """

    title = models.CharField(_('Название'), unique=True, max_length=100)
    rank = models.IntegerField(_('Позиция'), help_text=_('Очередность показа'), default=1)
    is_approved = models.BooleanField(_('Активно'), default=True)
    top_code = models.TextField(_('Код после <body>'), blank=True)
    bottom_code = models.TextField(_('Код перед </body>'), blank=True)
    header_code = models.TextField(_('Код в <header>'), blank=True)

    objects = CounterQuerySet.as_manager()

    class Meta:
        verbose_name = _('Счетчик')
        verbose_name_plural = _('Счетчики')
        ordering = ['is_approved', 'rank', 'title']

    def __str__(self):
        return self.title


class EmailSettings(SingletonModel):
    """
    Глобальные настройки почты
    """

    email = models.EmailField(_('Email'), max_length=255)
    password = models.CharField(_('Пароль'), max_length=255)
    port = models.PositiveSmallIntegerField(_('Порт'), default=587)
    tls = models.BooleanField(_('Использовать TLS'), default=True)
    host = models.CharField(_('Хост провайдера'), max_length=255)

    class Meta:
        verbose_name = _('Глобальные настройки почты')

    def __str__(self):
        return self.email


class EmailLogger(BaseModel):
    """
    Логи ошибок
    """

    message = models.TextField(_('Сообщение'))

    class Meta:
        verbose_name = _('Лог ошибок')
        verbose_name_plural = _('Логи ошибок')
        ordering = ['-created']

    def __str__(self):
        return str(self.id)

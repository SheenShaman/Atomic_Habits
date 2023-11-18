from django.db import models
from django.utils.translation import gettext as _

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    place = models.CharField(max_length=100, verbose_name=_('Place'), **NULLABLE)
    time = models.TimeField(verbose_name=_('Time'), **NULLABLE)
    action = models.CharField(max_length=250, verbose_name=_('Action'))

    is_pleasant_habit = models.BooleanField(verbose_name=_('Is_pleasant_habit'), default=False, **NULLABLE)
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL,
                                         verbose_name=_('Associated_habit'), **NULLABLE)
    frequency = models.PositiveIntegerField(default=1, verbose_name=_('Frequency'), **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name=_('Reward'), **NULLABLE)
    time_to_completed = models.PositiveIntegerField(default=2, verbose_name=_('Time_to_completed'), **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name=_('Is_public'))

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = _('Habit')
        verbose_name_plural = _('Habits')

# django
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

# models
from . import BaseModel

# other libraries
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

layer = get_channel_layer()


class Notification(BaseModel):
    """
    Base class for all notifications
    """
    # foreign keys
    user = models.ForeignKey(
        'User',
        related_name='notifications',
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )
    # optional
    message = models.CharField(max_length=300, blank=True)
    seen = models.BooleanField(
        _('seen'), default=False,
        help_text=_('Designates whether this notification has been seen '
                    'by the user.'),
    )


def send_notification(sender, instance, **kwargs):
    user = instance.user
    async_to_sync(layer.group_send)(
        user.id,
        {'type': 'notification', 'message': instance.message}
    )


post_save.connect(send_notification, sender=Notification)

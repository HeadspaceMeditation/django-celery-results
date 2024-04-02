"""Utilities."""
# -- XXX This module must not use translation as that causes
# -- a recursive loader import!

from django.conf import settings
from django.utils import timezone
import logging

# see Issue celery/django-celery#222
now_localtime = getattr(timezone, 'template_localtime', timezone.localtime)


def now():
    """Return the current date and time."""
    if getattr(settings, 'USE_TZ', False):
        return now_localtime(timezone.now())
    else:
        return timezone.now()

class disable_logging(object):
    """
    Within block, disable logging at or below the specified level.
    """
    def __init__(self, level=logging.WARNING):
        self.disabled_level = level

    def __enter__(self, *args, **kwargs):
        logging.disable(self.disabled_level)

    def __exit__(self, *args, **kwargs):
        logging.disable(logging.NOTSET)


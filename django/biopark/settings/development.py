"""Development extension settings."""
from biopark.settings.main import *  # noqa pylint: disable=W0614,W0401

DEBUG = True

THIRD_PARTY_APPS = [
    "django_extensions",
    "debug_toolbar",
]
THIRD_PARTY_APPS += ['behave_django']

INSTALLED_APPS += THIRD_PARTY_APPS   # NOQA

MIDDLEWARE += [     # NOQA
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda t: True,
}

INTERNAL_IPS = [
    "127.0.0.1",
]

COMPRESS_OFFLINE = False

try:
    LOGGING.update({})  # NOQA
except NameError:
    LOGGING = {}

LOGGING['loggers'].update({
    'celery.task': {
        'level': 'INFO',
        'handlers': ['console'],
        'propagate': True,
    },
    'celery.print': {
        'level': 'INFO',
        'handlers': ['console'],
        'propagate': True,
    },
})

# Actual Celery global variable names
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-worker_hijack_root_logger
worker_hijack_root_logger = False  # pylint: disable=invalid-name

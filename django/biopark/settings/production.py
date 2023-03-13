"""Production extension settings."""
import logging.config
import os
from pathlib import Path

from biopark.settings.main import *  # noqa pylint: disable=W0614,W0401

DEBUG = False

ALLOWED_HOSTS = ['*']

COMPRESS_OFFLINE = True

STATIC_ROOT = os.getenv('STATIC_ROOT')
MEDIA_ROOT = os.getenv('MEDIA_ROOT')

LOGFILE_ROOT = os.path.join(BASE_DIR, 'logs/production')  # NOQA
LOGFILE_ROOT = os.getenv('LOGS_ROOT', LOGFILE_ROOT)

info_file = os.path.join(LOGFILE_ROOT, 'django_info.log')
error_file = os.path.join(LOGFILE_ROOT, 'django_error.log')
debug_file = os.path.join(LOGFILE_ROOT, 'django_debug.log')

# Create log files if not exist
Path(info_file).touch(exist_ok=True)
Path(error_file).touch(exist_ok=True)
Path(debug_file).touch(exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(pathname)s:%(lineno)s] %(message)s',
        },
    },
    'filters': {
        'debug': {
            '()': 'biopark.log_filters.DebugFilter',
        },
        'info': {
            '()': 'biopark.log_filters.InfoFilter',
        },
        'error': {
            '()': 'biopark.log_filters.ErrorFilter',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'django.info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': info_file,
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 1,
            'filters': ['info']
        },
        'django.error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': error_file,
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 1,
            'filters': ['error']
        },
        'django.debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': debug_file,
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 1,
            'filters': ['debug']
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['django.info', 'django.error', 'django.debug'],
            'propagate': True,
        },
    }
}
logging.config.dictConfig(LOGGING)

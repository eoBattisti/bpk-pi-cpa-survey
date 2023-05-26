"""biopark main settings."""
# pylint: disable=useless-suppression,ungrouped-imports,too-many-lines
import os

from django.utils.translation import gettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists(os.path.join(BASE_DIR, 'secret_key.txt')):
    from django.core.management.utils import get_random_secret_key
    SECRET_KEY = get_random_secret_key()
    with open(os.path.join(BASE_DIR, 'secret_key.txt'), 'w', encoding='utf8') as f:
        f.write(SECRET_KEY)

with open(os.path.join(BASE_DIR, 'secret_key.txt'), 'r', encoding='utf8') as f:
    SECRET_KEY = f.read().strip()

DEBUG = True

HOST_URL = os.getenv('HOST_URL')

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ['http://localhost']

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = ['users.backend.EmailBackend']


APP_NAME = "BPK Survey"

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
]

THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    'widget_tweaks',
    "rest_framework",
    "django_filters",
    "auditlog",
    "compressor",
]

LOCAL_APPS = [
    'core',
    'axis',
    'exams',
    'questions',
    'users'
]


INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    'biopark.middleware.UserLanguageMiddleware'
]

ROOT_URLCONF = 'biopark.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 10,
}

# WSGI_APPLICATION = 'biopark.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DATABASE'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    },
}

# AUTH CONFIG
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Password reset
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
if os.getenv('EMAIL_PROTOCOL', 'tls') == 'ssl':
    EMAIL_USE_SSL = True
else:
    EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('pt-br', _('Portuguese')),
]
DEFAULT_LANGUAGE = 'pt-br'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public_static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_PRECOMPILERS = [
    ['text/x-sass', 'pysassc {infile} {outfile}'],
]
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # NOQA

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '{0}:{1}'.format(  # pylint: disable=consider-using-f-string
            os.getenv('MEMCACHED_HOST', 'memcached'),
            int(os.getenv('MEMCACHED_PORT', '11211')),
        ),
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'archive': {
            'format': '%(asctime)s (%(process)d) [%(levelname)s] %(module)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': True,
        },
    }
}
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

GRAPH_MODELS = {
  'app_labels': ['core', 'axis', 'exams', 'questions', 'users' ],
}

# Crispy Frontend Framework

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 60 * 24  # 1 day
CI = False

# flake8: noqa
from .base import *
from os.path import abspath, dirname, join


DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

INSTALLED_APPS += (
    'django_extensions',
)


SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='7nn(g(lb*8!r_+cc3m8bjxm#xu!q)6fidwgg&$p$6a+alm+x')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Process all tasks synchronously.
# Helpful for local development and running tests
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True


try:
    from .local import *
except ImportError:
    pass


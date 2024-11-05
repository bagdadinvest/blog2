# flake8: noqa
"""
Django settings for dentidelil project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from sys import path
from pathlib import Path
from storages.backends.azure_storage import AzureStorage
import os


BASE_DIR = Path(__file__).resolve().parent.parent

import environ
env = environ.Env()

# Absolute filesystem path to the top-level project folder:

root = environ.Path(__file__) - 3
PROJECT_ROOT = root()

environ.Env.read_env(root('.env'))

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = root.path('dentidelil')

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Do not set SECRET_KEY or LDAP password or any other sensitive data here.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', True)

ALLOWED_HOSTS = ['*']

AZURE_TRANSLATOR_KEY = env('AZURE_TRANSLATOR_KEY', default='')
AZURE_TRANSLATOR_ENDPOINT = 'https://api.cognitive.microsofttranslator.com/'

# Application definition

# Existing INSTALLED_APPS and MIDDLEWARE configuration
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'compressor',
    'taggit',
    'modelcluster',
    'django_distill',
    'websites',
    'topblogs',

    'foundation_formtags',
    'storages',
    'blog',
    'contact',
    'documents_gallery',
    'gallery',
    'pages',
    'people',
    'products',
    'search',
    'users',
    'utils',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.search_promotions',
    'wagtail.search.backends.database',
    'wagtail.contrib.settings',
    "wagtail_localize",
    "wagtail_localize.locales",
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.modeladmin',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtailmedia',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail_feeds',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.linkedin',
    'rosetta',
    'debug_toolbar',
)

ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_MESSAGES_PER_PAGE = 500
AZURE_CLIENT_SECRET = env('AZURE_CLIENT_SECRET', default='')

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
   # 'django_brotli.middleware.BrotliMiddleware',  # Add Brotli Middleware here
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'dentidelil.middleware.LanguageRedirectMiddleware',  # Include the path to your middleware  # should be after SessionMiddleware and before CommonMiddleware
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'dentidelil.settings.middleware.CustomDebugToolbarMiddleware',  # Replace this with the correct path
    'dentidelil.middleware.CatchAllExceptionsMiddleware',

)

INTERNAL_IPS = [
    '127.0.0.1',  # Or 'localhost'
]

BROTLI_EXCLUDE_CONTENT_TYPES = [
    'image/png',
    'image/jpeg',
    'image/gif',
    'application/pdf',
    'application/octet-stream',  # General binary files
]

BROTLI_MIDDLEWARE = {
    'GZIP_COMPRESSLEVEL': 6,  # Set gzip compression level (0-9)
    'BROTLI_COMPRESSLEVEL': 4,  # Set Brotli compression level (0-11)
    'GZIP_MIN_LENGTH': 1024,   # Minimum response size in bytes to trigger gzip
    'BROTLI_MIN_LENGTH': 1024, # Minimum response size in bytes to trigger Brotli
}

ROOT_URLCONF = 'dentidelil.urls'

ADMINS = (
    ("""lotfikanouni""", 'lotfikanouni4@gmail.com'),
)

MANAGERS = ADMINS

ROSETTA_TRANSLATION_SUGGESTIONS = {
    'AZURE': {
        'API_KEY': env('ROSETTA_AZURE_API_KEY', default=''),
        'ENDPOINT': 'https://api.cognitive.microsofttranslator.com/',
        'REGION': 'uaenorth'  # Example: 'westeurope'
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',  # Add this line
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'dentidelil.wsgi.application'

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

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'account_login'

ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'users.adapters.SocialAccountAdapter'

ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'account_login'

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.HalloRichTextArea'
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(root('db.sqlite3')),  # or just 'db.sqlite3' for simplicity
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
WAGTAIL_I18N_ENABLED = True

USE_L10N = True
USE_TZ = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('en', 'English'),
    ('fr', "French"),
    ('es', "Spanish"),
    ('ar', 'Arabic'),
    ('tr', 'Turkish'),
    ('de', 'German'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('hu', 'Hungarian'),
    ('ru', 'Russian'),
]
WAGTAILLOCALIZE_SYNC_TREE = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

STATIC_ROOT = root('static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_CACHEABLE_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_OFFLINE = False

GOOGLE_MAPS_KEY = ''
DYNAMIC_MAP_URL = ''
STATIC_MAP_URL = ''

LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

WAGTAIL_SITE_NAME = "dentidelil"

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    },
}

BROKER_URL = 'redis://127.0.0.1:6379/0'

CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_COLOR = False

CACHEOPS_REDIS = "redis://127.0.0.1:6379/1"

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,  # If Redis is down, fall back to default behavior
        }
    }
}

CACHEOPS = {
    'wagtailcore.page': {'ops': 'all', 'timeout': 60 * 15},  # Cache all operations on Page for 15 minutes
    'wagtailcore.*': {'ops': 'all', 'timeout': 60 * 15},     # Cache all models in wagtailcore
    'wagtailimages.image': {'ops': 'all', 'timeout': 60 * 60},
    'wagtailimages.uploadedimage': {'ops': 'all', 'timeout': 60 * 60},
    'wagtailmedia.media': {'ops': 'all', 'timeout': 60 * 30},
    'blog.*': {'ops': 'all', 'timeout': 60 * 10},            # Cache all blog models for 10 minutes
}

CACHEOPS_LOGGING = True
CACHEOPS_DEGRADE_ON_FAILURE = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

WAGTAILLOCALIZE_MACHINE_TRANSLATOR = {
    "CLASS": "translations.azure.AzureTranslator",
    "OPTIONS": {
        'subscription_key': env('AZURE_TRANSLATOR_SUBSCRIPTION_KEY', default=''),
        'region': 'uaenorth',
    }
}


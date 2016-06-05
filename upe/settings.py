"""
Django settings for upe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9+!w(w9&qra8zp)k(^xq%i!3flgnipy4m_84&o8bf7#&&4nvl!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = False



LOGIN_URL = '/login/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markdown',
    'django_mathjax',
    'website',
    'upe_calendar',
    'users'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'upe.urls'

WSGI_APPLICATION = 'upe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
    #'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'upe_db',
        'USER': 'admin',
        'PASSWORD': 'littlewhale',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    #'default': {
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'upe_db',
        'USER': 'admin',
        'PASSWORD': 'littlewhale',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Media files (Images, Downloads, Files)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = ('users.backends.CustomBackend',)

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ("website.processor.populate_footer",)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST      = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT      = 25
EMAIL_USE_TLS   = False
DEFAULT_FROM_EMAIL  = 'Do-Not-Reply <atlantis@upe.cs.berkeley.edu>'

MATHJAX_ENABLED=True

MATHJAX_CONFIG_DATA = {
  "tex2jax": {
    "inlineMath":
      [
          ['\\(','\\)']
      ]
  }
}

MARKDOWN_EXTENSIONS = ['extra']


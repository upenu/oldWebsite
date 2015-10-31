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
SOCIAL_AUTH_FACEBOOK_KEY = '1636610166620222'
SOCIAL_AUTH_FACEBOOK_SECRET = 'cdee9718c25fa87dec38022246af441a'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '408450188124-m8m6fg1qk6jghqsuuftktf96qso7bhg2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'u4yC9izdYi8P4Rpku5aNPj2X'
SOCIAL_AUTH_TWITTER_KEY = '2V9j8no3cwZbaaLGRO8Hy7yhF'
SOCIAL_AUTH_TWITTER_SECRET = '8UUUipY2a2VlHjfgrkgZz6NLGnNv7EcEoIQjmG6uOhyjD8m4L4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = '/login/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'upe_calendar',
    'users',
    'social.apps.django_app.default'
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

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'upe_db',
        'USER': 'admin',
        'PASSWORD': 'littlewhale',
        'HOST': '127.0.0.1',
        'PORT': '5432',
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'users.backends.CustomBackend',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    )

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ("website.processor.populate_footer",)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST      = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT      = 25
EMAIL_USE_TLS   = False
DEFAULT_FROM_EMAIL  = 'Do-Not-Reply <atlantis@upe.cs.berkeley.edu>'


# For facebook/google/twitter
LOGIN_REDIRECT_URL = '/'

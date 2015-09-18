"""
Django settings for dajs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'ws4redis.context_processors.default',
)

LOGIN_URL = '/sports-store-admin/login'
LOGIN_REDIRECT_URL = '/sports-store-admin/'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../dajs/sports_store/templates'),
    os.path.join(BASE_DIR, '../dajs/sportsstoreadmin/templates'),
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

WEBSOCKET_URL = '/ws/'
WS4REDIS_PREFIX = 'demo'
WS4REDIS_EXPIRE = 7200
# WS4REDIS_SUBSCRIBER = 'dajs.redis_store.RedisSubscriber'
WSGI_APPLICATION = 'ws4redis.django_runserver.application'
WS4REDIS_HEARTBEAT = '--heartbeat--'
# WSGI_APPLICATION = 'dajs.wsgi.application'
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_PREFIX = 'session'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_ALLOW_ALL = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')w#hci8pc_=@nj6_kim4jl!2%@3a8)4n27x=l(@v947^!3s1f_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
    'dajs',
    'sports_store',
    'sportsstoreadmin',
    'ajsexample',
    'dygraphsex',
    'rest_framework',
    'corsheaders',
    'djangular',
    'ws4redis',
    'chatserver',
)

MIDDLEWARE_CLASSES = (
    'djangular.middleware.DjangularUrlMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'dajs.urls'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'

STATICFILES_DIRS = ('./dajs/static', './sports_store/static')

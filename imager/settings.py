"""
Django settings for imager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from configurations import Settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

class Base(Settings):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    USER_NAME = os.environ.get('USER')

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'mj)xs(k)0^9xt!ah-0nc^&03l%cpsq2!p#hq9)3i2why&ynyd('

    # SECURITY WARNING: don't run with debug turned on in production!

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'dimager',
        'imager_images',
        'registration',

    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'imager.urls'
    WSGI_APPLICATION = 'imager.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'djangoimager',
            'USER': 'aabulota',
        }
    }

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "imager/static"),
    )
    TEMPLATES_DIRS = [
        os.path.join(BASE_DIR, "/django-imager/imager/templates"),
    ]
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ACCOUNT_ACTIVATION_DAYS = 3
    REGISTRATION_AUTO_LOGIN = True
    REGISTRATION_OPEN = True
    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/profile/'


class Dev(Base):
    DEBUG = True
    TEMPLATE_DEBUG = True
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Prod(Base):
    import dj_database_url
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DEBUG = False
    TEMPLATE_DEBUG = False
    DATABASES = {
                'default': dj_database_url.config()
                }

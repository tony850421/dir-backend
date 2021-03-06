"""
Django settings for tutorial2 project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$o%*ndnb&1n7!j&*!a!_b$qyowzyj47r!ai8m=ahgno9f4jy8a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_HTTPONLY = False

# CORS_EXPOSE_HEADERS = ('Set-Cookie')
# SESSION_COOKIE_DOMAIN = '.dir.com'
# SESSION_COOKIE_NAME = "tonycookiename"

# CORS_ORIGIN_WHITELIST = [
#     'www.api.dir.com',
#     'www.dir.com',
#     'dir.com',
#     'api.dir.com',
# ]

LOGIN_REDIRECT_URL = ('../..')

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 10
# }

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'snippets',
    'tracking',
    'django_apscheduler',
    # 'social.apps.django_app.default', #add this to installed apps
    # 'social_django',  # django social auth
    # 'rest_social_auth',
)

#Email
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dirstuff'
EMAIL_HOST_PASSWORD = 'dirstuffdirstuff1234,.'
# EMAIL_USE_TLS = True

MIDDLEWARE_CLASSES = (
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'tutorial2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# SOCIAL_AUTH_FACEBOOK_KEY = '128874921166794' #myfirstapp
# SOCIAL_AUTH_FACEBOOK_SECRET = '368776d7bbad5dc969e7e57eb6486215'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', ]  # optional
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}  # optional

# REST_SOCIAL_OAUTH_REDIRECT_URI = '/'
# REST_SOCIAL_DOMAIN_FROM_ORIGIN = True

AUTHENTICATION_BACKENDS = (
 # 'social_core.backends.facebook.FacebookOAuth2',
 # 'social.backends.facebook.FacebookAppOAuth2',
 # 'social.backends.facebook.FacebookOAuth2',
 'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'tutorial2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
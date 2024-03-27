"""
Django settings for flowersdirect project.

Generated by 'django-admin startproject' using Django 2.1.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w4ze7pr8&e=l2em=e-dmhvvl!#i#^vx8jus#a0dpdjjfg#b+e%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#CSRF_TRUSTED_ORIGINS = ['']
ALLOWED_HOSTS = ['5428f7a2bede4b29b6a85b623da9cae0.vfs.cloud9.eu-west-1.amazonaws.com']

#CSRF_TRUSTED_ORIGINS = ['https://5428f7a2bede4b29b6a85b623da9cae0.vfs.cloud9.eu-west-1.amazonaws.com','http://x23219203-flowersdirect-env.eba-dufixdmm.eu-west-1.elasticbeanstalk.com']
#ALLOWED_HOSTS = ['5428f7a2bede4b29b6a85b623da9cae0.vfs.cloud9.eu-west-1.amazonaws.com','x23219203-flowersdirect-env.eba-dufixdmm.eu-west-1.elasticbeanstalk.com']

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',    
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

INSTALLED_APPS = [
    'buyer',
    'seller',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'crispy_forms',
    'crispy_bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware"
    
]

ROOT_URLCONF = 'flowersdirect.urls'

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

WSGI_APPLICATION = 'flowersdirect.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
} 

''' DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'flowers-direct',
        'USER': 'postgres',
        'PASSWORD': '1Password',
        'HOST': 'flowers-direct-app.chwlezgyi7rm.eu-west-1.rds.amazonaws.com',
        'PORT': '5432',
    }
} '''

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
SITE_ID = 1

ACCOUNT_ADAPTER = 'seller.account_adapter.NoNewUsersAccountAdapter'
LOGIN_REDIRECT_URL = 'dashboard'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
ACCOUNT_ADAPTER = 'seller.account_adapter.NoNewUsersAccountAdapter'


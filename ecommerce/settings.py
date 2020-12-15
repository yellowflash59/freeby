"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tu52+-tlq+4x(j(ku!d_575_7^tv+ud0++gzfsa-eaf(!rc7)s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DEFAULT_FROM_EMAIL="coding with flash <@gmail.com>"


EMAIL_HOST= "smtp.gmail.com"
EMAIL_HOST_USER="@gmail.com"
EMAIL_HOST_PASSWORD="*****"
EMAIL_PORT=587
EMAIL_USE_TLS=True

SITE_URL="http://freeby.com"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'carts',
    'orders',
    'localflavor',
    'marketing.apps.MarketingConfig',
    'accounts.apps.AccountsConfig',
    'stripe'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marketing.middleware.DisplayMarketingMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MARKETING_HOURS_OFFSET=3
MARKETING_SECONDS_OFFSET=0

TEMPLATE_CONTEXT_PROCESSORS=(
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.request',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL= '/media/'

MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),'static','media')

STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),'static','static_root')

STATICFILES_DIRS=(
    os.path.join(os.path.dirname(BASE_DIR),'static','static_files'),
)

STRIPE_SECRET_KEY="sk_test_51Guxm2ClRwhSe2klCREowvA2olzZTKLTkWNjK0wg5NuakejWdbnvWxWRBMV7BqRtpn1JY7yqtLSWSWcY9KRA7ssi00iHy9wUkp"
STRIPE_PUBLISHABLE_KEY="pk_test_51Guxm2ClRwhSe2klk5PB8zOQQiZdfw5SccJtUMojikdobn7EK5MmEKUCRNNJi7RxC2HFL8pUrvvs5OfgaCoCgH6S00WugakF46"
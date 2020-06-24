
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eq9vwx6-&tk1=_&mb6a#78*06=nlb5v1kk*@qwlh54d-*y-cd_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #ignoreline

ALLOWED_HOSTS = ['134.209.229.24','www.elra3i.com','elra3i.com','127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'import_export',
    'django_countries',
    'tinymce',
    'product',
    'settings',
    'charts',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
    'designer',
    'payment',
    'paypal.standard.ipn',
    'clients',
    'administration',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'elraei',
            'USER': 'ahmed',
            'PASSWORD': 'Mido@2059',
            'HOST':'localhost',
            'PORT':'',
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

LOCALE_PATHS = [
    os.path.join(BASE_DIR,'locale')
]

LANGUAGES = [
    ('en','English'),
    ('ar','Arabic'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/home/ahmedhatem/var/www/static/',
]

if not DEBUG:
    STATIC_ROOT = '/home/ahmedhatem/var/www/static/'


MEDIA_URL  = '/media/'
MEDIA_ROOT = '/home/ahmedhatem/var/www/media/'

''' TINYMCE_JS_URL = os.path.join(STATIC_URL, "django_tinymce/init_tinymce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "django_tinymce")
 '''
#Auth
AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ACCOUNT_FORMS = { 
'signup': 'clients.forms.CustomSignupForm', 
} 

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

## Braintree Settings

if DEBUG:
    PAYPAL_TEST = True
    PAYPAL_RECEIVER_EMAIL = "ahmedelrai18@gmail.com"
    BT_ENVIRONMENT = 'sandbox'
    BT_MERCHANT_ID = 'sds9ktn32h9vsc8g'
    BT_PUBLIC_KEY  = '7wpczxwhcv8d3xch'
    BT_PRIVATE_KEY = '46b090eaa9ae0e835d01664c6eb20962'
else:
    PAYPAL_RECEIVER_EMAIL = "ahmedelrai18@gmail.com"
    BT_ENVIRONMENT = 'sandbox'
    BT_MERCHANT_ID = ''
    BT_PUBLIC_KEY  = ''
    BT_PRIVATE_KEY = ''

### DRF SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
#-*- coding: utf-8 -*-
from .base import *

# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'cities',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'cars',
    'citizens',
    'drivers',
    'trips',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cabsy',
        'USER': 'cabsy',
        'PASSWORD': 'mysecurepass',
        'HOST': '0.0.0.0',
        'PORT': '5436',
    }
}

# SOCIAL AUTH CONFIGURATIONS
#AUTHENTICATION_BACKENDS = (
#    'social_auth.backends.facebook.FacebookBackend',
#    'allauth.account.auth_backends.AuthenticationBackend',
#)

AUTH_USER_MODEL = 'citizens.Citizen'
#FACEBOOK_APP_ID = '257746231293590'
#FACEBOOK_API_SECRET = 'a32920fa1fce946b3be1a09b4ba6c03a'
#SOCIAL_AUTH_USER_MODEL = 'citizens.Citizen'

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}}

# TEMPLATES CONFIGURATIONS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                #"allauth.account.context_processors.account",
                #"allauth.socialaccount.context_processors.socialaccount",
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#STATIC CONFIGURATIONS 
STATIC_URL = '/static/'

#MEDIA CONFIGURATIONS
MEDIA_ROOT = os.path.join(BASE_DIR, '../media/')
MEDIA_URL = '/media/'

SITE_ID = 1

# PROJECT CONSTANTS
STATES_MEXICO = (
    ('1', 'Aguascalientes'),
    ('2','Baja California'),
    ('3', 'Baja California Sur'),
    ('4', 'Campeche'),
    ('5', 'Coahuila de Zaragoza'),
    ('6', 'Colima'),
    ('7', 'Chiapas'),
    ('8', 'Chihuahua'),
    ('9', 'Distrito Federal'),
    ('10', 'Durango'),
    ('11', 'Guanajuato'),
    ('12', 'Guerrero'),
    ('13', 'Hidalgo'),
    ('14', 'Jalisco'),
    ('15', 'México'),
    ('16', 'Michoacán de Ocampo'),
    ('17', 'Morelos'),
    ('18', 'Nayarit'),
    ('19', 'Nuevo León'),
    ('20', 'Oaxaca'),
    ('21', 'Puebla'),
    ('22', 'Querétaro'),
    ('23', 'Quintana Roo'),
    ('24', 'San Luis Potosí'),
    ('25', 'Sinaloa'),
    ('26', 'Sonora'),
    ('27', 'Tabasco'),
    ('28', 'Tamaulipas'),
    ('29', 'Tlaxcala'),
    ('30', 'Veracruz de Ignacio de la Llave'),
    ('31', 'Yucatán'),
    ('32', 'Zacatecas'),
)

COMPLIMENTS_SUBJECT = (
    ('1', 'Higiene Personal'),
    ('2', 'Estado la unidad'),
    ('3', 'Conduccion'),
    ('4', 'Trato con el cliente'),
    ('5', 'Ruta'),
)

COMPLAINTS_SUBJECT = (
    ('1', 'Higiene Personal'),
    ('2', 'Estado la unidad'),
    ('3', 'Conduccion'),
    ('4', 'Trato con el cliente'),
    ('5', 'Ruta'),
    ('6', 'Actitud Sospechosa'),
)

DRIVER_STATUS = (
    ('A', 'Activo'),
    ('S', 'Suspendido'),
    ('R', 'Re-Incorporado'),
    ('P', 'Pendiente'),
)
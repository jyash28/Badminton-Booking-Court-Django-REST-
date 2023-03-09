from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
DEV = DEBUG

INSTALLED_APPS += ('debug_toolbar',)


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'badminton',
		'USER': 'postgres',
		'PASSWORD': 'postgres',
		'HOST': '',
		'PORT': '',
	}
}


MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

SECRET_KEY = 'devel'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 2

AUTH_PASSWORD_VALIDATORS = []

INTERNAL_IPS = ("127.0.0.1",)


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
    "basic": {
    'type':'basic'
    }
    },
    'USE_SESSION_AUTH': True,
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type':'apiKey',
            'in':'header',
            'name':'authorization'
        }
    },
    "app_name":'rest_framework',
    # 'LOGIN_URL':'/api/v1/login/',
    'LOGOUT_URL':'rest_framework:logout',
    'DOC_EXPANSION': None,
    'SHOW_REQUEST_HEADERS':True,
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION':'list',
    # The method list in the interface document is sorted in ascending order
    'APIS_SORTER':'alpha',
    # If json submission is supported, the interface document contains json input box
    'JSON_EDITOR': True,
    # Method list alphabetical order
    'OPERATIONS_SORTER':'alpha',
    'VALIDATOR_URL': None,
}
# LOGIN_URL ='accounts/login'
LOGOUT_URL ='accounts/logout'
LOGIN_URL = 'rest_framework:login'



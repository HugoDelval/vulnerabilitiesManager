"""
Django settings for webSite project.

Generated by 'django-admin startproject' using Django 1.8.3.

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
SECRET_KEY = 'ksd%eg$s-98m@002odcd*&1sv!!g9&ya^2ciq&+rc)(=f^kg(1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userManager',
    'vuln',
    'docxImgAnonymisateur',
    'LTE',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'webSite.urls'

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
                "django.core.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = 'webSite.wsgi.application'


from . import databases
DATABASES = databases.getDatabaseConfig()

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
STATIC_ROOT = '/home/hdl/KM/vulnerabilitiesManager/webSite/static/'

GRAPPELLI_ADMIN_TITLE = 'KMAmossys'

# UserManager
LOGIN_URL = '/user/login/'


########################
## LDAP configuration ##
########################

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
#AUTH_LDAP_SERVER_URI = "ldap://ldap.amossys.fr"
AUTH_LDAP_SERVER_URI = "ldap://127.0.0.1"

import ldap
from django_auth_ldap.config import LDAPSearch

AUTH_LDAP_BIND_DN = "" # ex : "cn=django-agent,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=amo,dc=test,dc=com", ldap.SCOPE_SUBTREE, "(cn=%(user)s)")
# or perhaps:
# AUTH_LDAP_USER_DN_TEMPLATE = "cn=%(user)s,dc=amo,dc=test,dc=com"


# chiffrer les communications
# AUTH_LDAP_START_TLS = True

# fait correspondre les champs du ldap avec les champs du User local
AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn", "username": "cn"}
# idem mais avec des booleens
# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "cn=active,ou=groups,dc=example,dc=com",
#     "is_staff": ["cn=staff,ou=groups,dc=example,dc=com",
#                  "cn=admin,ou=groups,dc=example,dc=com"],
#     "is_superuser": "cn=superuser,ou=groups,dc=example,dc=com"
# }


AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}
import logging

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
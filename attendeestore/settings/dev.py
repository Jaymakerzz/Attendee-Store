from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5(su@dlxyxzo8-96xav!wdlq!!!2*1#l9&cx(b29l*ixvqo1v3'

# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'attendeelist',
        'USER': 'root',
        'PASSWORD': 'Nn@01840617',
        'HOST': 'localhost',
    }
}

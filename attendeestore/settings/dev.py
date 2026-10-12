import os
from dotenv import load_dotenv
from .common import *

load_dotenv()

DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-insecure-key")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'attendeelist',
        'USER': 'root',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost',
    }
}

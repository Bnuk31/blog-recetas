from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Nicou813$default',
        'USER': 'Nicou813',
        'PASSWORD': 'rootroot',
        'HOST': 'Nicou813.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['rodrigodg91.pythonanywhere.com',
                'Nicou813.pythonanywhere.com']

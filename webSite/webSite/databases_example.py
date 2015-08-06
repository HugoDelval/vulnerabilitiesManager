def getDatabaseConfig():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kmbdd',
            'HOST': 'localhost',
            'PASSWORD': '',
            'PORT': '',
            'USER': 'root',
        }
    }
    return DATABASES

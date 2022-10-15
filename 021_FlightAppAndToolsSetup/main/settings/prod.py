from .base import *
# on Live:
DEBUG = False
ALLOWED_HOSTS = [
    '127.0.0.1',
]

INSTALLED_APPS += [
    
]

MIDDLEWARE += [
    
]

'''
# PostreSQL:
DATABASES = { 
    "default": { 
        "ENGINE": "django.db.backends.postgresql_psycopg2", 
        "NAME": config("POSTGRESQL_DATABASE"), 
        "USER": config("POSTGRESQL_USER"), 
        "PASSWORD": config("POSTGRESQL_PASSWORD"), 
        "HOST": config("POSTGRESQL_HOST"), 
        "PORT": config("POSTGRESQL_PORT"), 
        "ATOMIC_REQUESTS": True, 
    }
}
'''
# SQLite:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_live.sqlite3',
    }
}
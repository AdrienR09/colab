from .base import *
import dj_database_url

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zaj=iz3!w_469o1u0=(knxenr+*)+=4rojj=g+s#y*)$$g8#c)'#os.environ.get('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['vite-ma-table.com', 'www.vite-ma-table.com', 'https']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'supq4170_colab',
        'USER': 'supq4170_AdrienR09',
        'PASSWORD': 'zriiPeWTpQfz',
        'HOST': '',
        'PORT': '3306',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "colab/media")
MEDIA_URL = 'media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "colab/static")
STATIC_URL = "/static/"
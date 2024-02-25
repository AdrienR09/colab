from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!#6si^t9druun1kp!ie_4d8pz9-i+fi27h4*k=ic%-@k=jx^#c"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

try:
    from .local import *
except ImportError:
    pass

#EMAIL_HOST = "<your email host>"                    # smtp-relay.sendinblue.com
#EMAIL_USE_TLS = False                               # False
#EMAIL_PORT = "<your email port>"                    # 587
#EMAIL_HOST_USER = "<your email user>"               # your email address
#EMAIL_HOST_PASSWORD = "<your email password>"       # your password
#DEFAULT_FROM_EMAIL = "<your default from email>"    # email ending with @sendinblue.com

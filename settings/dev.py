# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6j(*v8hi@gc1(bl-3896n25*h_#t^=&9=wt$jfojcf43@n8vg!'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .base import *
except ImportError:
    pass

DEBUG = False
TEMPLATE_DEBUG = False


try:
    from .base import *
except ImportError:
    pass

SECRET_KEY = 'vintages'

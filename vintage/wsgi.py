"""
WSGI config for vintage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import sys
import os
import site

from django.core.wsgi import get_wsgi_application


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('~/.virtualenvs/vintage/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('~/www/vintage')
sys.path.append('~/www/vintage/vintage')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vintage.settings")

application = get_wsgi_application()

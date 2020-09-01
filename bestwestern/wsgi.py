"""
WSGI config for bestwestern project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

environment = os.environ.get('PROJECT_ENV', 'development')

print (os.environ.get('PROJECT_ENV'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestwestern.settings.{}'.format(environment))

application = get_wsgi_application()

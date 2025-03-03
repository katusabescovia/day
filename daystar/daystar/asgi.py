"""
ASGI config for daystar project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the correct path to the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'daystar.settings')

application = get_wsgi_application()

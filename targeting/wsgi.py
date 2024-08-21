"""
WSGI config for targeting project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dtale.app import build_app
from data_quality.dispatcher import PathDispatcher  # replace 'data_quality' with your actual app name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'targeting.settings')  # replace 'targeting' with your actual project name

def make_app(prefix):
    if prefix == 'flask':
        return build_app(app_root='/flask', reaper_on=False)

application = PathDispatcher(get_wsgi_application(), make_app)
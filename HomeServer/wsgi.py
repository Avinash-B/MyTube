"""
WSGI config for HomeServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeServer.settings')

application = get_wsgi_application()
# application = WhiteNoise(application, root='/static/')

#Add this line in case you have more than on estatic files
# application.add_files('/path/to/more/static/files', prefix='more-files/')
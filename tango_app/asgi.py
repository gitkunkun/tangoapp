"""
ASGI config for tango_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# load_dotenv を追加
from dotenv import load_dotenv

load_dotenv()

# "flea_market_app.settings.dev" に変更
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_app.settings.dev")

application = get_asgi_application()
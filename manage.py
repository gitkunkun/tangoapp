#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # load_dotenv を追加
    from dotenv import load_dotenv

    load_dotenv()

    # "flea_market_app.settings.dev" に変更
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_app.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
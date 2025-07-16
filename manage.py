#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # set environment variables
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storeproject.settings")
    os.environ.setdefault("DJANGO_SECRET_KEY", "django-insecure-k&2x)%0ca*9+l^c@k*-*c9bj3j7)sgklvp=b2+p&n@rc#&w&7y")
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

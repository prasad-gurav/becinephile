"""
Django settings entrypoint.

Use: DJANGO_SETTINGS_MODULE=conf.settings (when run from becinephile/)
     or becinephile.conf.settings (when run from repo root with PYTHONPATH).
"""
from split_settings.tools import include

include("base.py")

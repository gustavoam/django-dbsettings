from __future__ import absolute_import
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'dbsettings'

    def ready(self):
        from dbsettings.values import *  # NOQA
        from dbsettings.group import *  # NOQA

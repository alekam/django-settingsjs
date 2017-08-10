from __future__ import print_function

import json
import sys
import re
from types import ModuleType
from collections import OrderedDict

from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import RegexURLPattern, RegexURLResolver
from django.core.management.base import BaseCommand
from django.conf import settings
from django.template.loader import render_to_string

from settingsjs import signals
from settingsjs.utils import get_js_settings


class Command(BaseCommand):
    help = u'Create settings.js file'

    def handle(self, *args, **opts):
        try:
            file_path = getattr(settings, 'SETTINGSJS_GENERATED_FILE')
        except:
            raise ImproperlyConfigured('You should provide SETTINGSJS_GENERATED_FILE setting.')

        # output to the file
        file_ = open(file_path, "w+")
        file_.write(self.get_file_contents())
        file_.close()

        if opts['verbosity'] > 0:
            print("Done generating Javascript urls file %s" % file_path)

    def get_file_contents(self):
        return render_to_string('settingsjs/settings.js',
                                {'jssettings': self.get_js_settings()})

    def get_js_settings(self):
        jssettings = get_js_settings()

        signals.collect_settings.send(
            sender=self,
            jssettings=jssettings,
            request=None
        )

        return jssettings

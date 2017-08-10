# coding: utf-8

from django.conf import settings


def get_js_settings():
    jssettings = {}

    keys = getattr(settings, 'SETTINGS_JS_KEYS', None)
    if keys:
        for key in keys:
            jssettings[key] = getattr(settings, key, None)

    if hasattr(settings, 'SETTINGS_JS'):
        jssettings.update(settings.SETTINGS_JS)

    return jssettings

import json

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

from . import signals
from .utils import get_js_settings


def settings_js(request, extra_context=None):
    mimetype = 'text/javascript'

    context = RequestContext(request)
    if extra_context is not None:
        context.update(extra_context)

    jssettings = getattr(context, 'settings', {})

    data = get_js_settings()
    if data:
        jssettings.update(data)

    signals.collect_settings.send(
        sender=settings_js,
        jssettings=jssettings,
        request=request
    )

    context.update({
        'settings': jssettings,
        'jssettings': json.dumps(jssettings)
    })

    return render_to_response('settingsjs/settings.js', context, mimetype=mimetype)

# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import get_model

def aloha_init(request):
    """
    Build the javascript file which is initializing the aloha-editor
    Run the javascript code for the AlohaInput widget
    """
    
    links = []
    link_models = getattr(settings, 'DJALOHA_LINK_MODELS', ())
    for full_model_name in link_models:
        app_name, model_name = full_model_name.split('.')
        model = get_model(app_name, model_name)
        if model:
            links.extend(model.objects.all())
    aloha_version = getattr(settings, 'DJALOHA_ALOHA_VERSION', "aloha.0.20.20")
    template_name = 'djaloha/aloha_%s_init.js' % aloha_version

    jquery_no_conflict = getattr(settings, 'DJALOHA_JQUERY_NO_CONFLICT', False)

    return render_to_response(
        template_name,
        {
            'links': links,
            'config':{
                'jquery_no_conflict': jquery_no_conflict
            }
        },
        mimetype='text/javascript',
        context_instance=RequestContext(request)
    )

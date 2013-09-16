# -*- coding: utf-8 -*-
from distutils.version import LooseVersion
from floppyforms.widgets import TextInput
from django.forms import Media
from django.core.urlresolvers import reverse
from django.conf import settings


class AlohaInput(TextInput):
    """
    Text widget with aloha html editor
    requires floppyforms to be installed
    """

    template_name = 'djaloha/alohainput.html'

    def __init__(self, *args, **kwargs):
        kwargs.pop('text_color_plugin', None) # for compatibility with previous versions
        self.aloha_plugins = kwargs.pop('aloha_plugins', None)
        self.extra_aloha_plugins = kwargs.pop('extra_aloha_plugins', None)
        self.aloha_init_url = kwargs.pop('aloha_init_url', None)
        super(AlohaInput, self).__init__(*args, **kwargs)

    def _get_media(self):
        """
        return code for inserting required js and css files
        need aloha , plugins and initialization
        include the 3rd party ImagePlugin from tapo: make possible to drag-and-drop and edit images
        """

        try:
            aloha_init_url = self.aloha_init_url or getattr(settings, 'DJALOHA_INIT_URL', None) or reverse('aloha_init')
            aloha_version = getattr(settings, 'DJALOHA_ALOHA_VERSION', "aloha.0.20.20")

            aloha_plugins = self.aloha_plugins
            if not aloha_plugins:
                aloha_plugins = getattr(settings, 'DJALOHA_PLUGINS', None)
            if not aloha_plugins:
                aloha_plugins = (
                    "common/format",
                    "common/highlighteditables",
                    "common/list",
                    "common/link",
                    "common/undo",
                    "common/paste",
                    "common/commands",
                    "common/contenthandler",
                    "common/image",
                    "common/align",
                    #"extra/attributes",
                    "common/characterpicker",
                    #"common/abbr",
                    "common/horizontalruler",
                    "common/table",
                )
            if self.extra_aloha_plugins:
                aloha_plugins = tuple(aloha_plugins) + tuple(self.extra_aloha_plugins)

            css = {
                'all': (
                    "{0}/css/aloha.css".format(aloha_version),
                )
            }

            js = []

            skip_jquery = getattr(settings, 'SKIP_DJALOHA_JQUERY', False)
            if not skip_jquery:
                if settings.DEBUG:
                    js.append(getattr(settings, 'DJALOHA_JQUERY', "js/jquery-1.7.2.js"))
                else:
                    js.append(getattr(settings, 'DJALOHA_JQUERY', "js/jquery-1.7.2.min.js"))

            if LooseVersion(aloha_version) >= LooseVersion('aloha.0.22'):
                js.append("{0}/lib/require.js".format(aloha_version))

            js.append(aloha_init_url)
            js.append(u'{0}/lib/aloha.js" data-aloha-plugins="{1}'.format(aloha_version, u",".join(aloha_plugins)))
            js.append('djaloha/js/djaloha-init.js')


            return Media(css=css, js=js)
        except Exception, msg:
            print '## AlohaInput._get_media Error ', msg

    media = property(_get_media)

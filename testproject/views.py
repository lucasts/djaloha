# -*- coding: utf-8 -*-

from django import forms
from django.views.generic.edit import FormView
from djaloha.widgets import AlohaInput


class DjalohaForm(forms.Form):
    body = forms.CharField(widget=AlohaInput)

sample_form_view = FormView.as_view(template_name='form.html', form_class=DjalohaForm)

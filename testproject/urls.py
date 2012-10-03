# -*- coding: utf-8 -*-
from django.conf.urls import *
from testproject.views import sample_form_view


urlpatterns = patterns('',
    url('^', include('djaloha.urls')),
    url('sample.html', sample_form_view),
)

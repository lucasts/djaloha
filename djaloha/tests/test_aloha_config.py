#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from djaloha.views import aloha_init

class AlohaConfigTest(TestCase):


    def setUp(self):
        super(AlohaConfigTest, self).setUp()
        self.url = reverse('aloha_init')
        self.response = self.client.get(self.url)

    def test_should_respond_correctly(self):
        self.assertEqual(self.response.status_code, 200)

    def test_should_inherit_the_base_template(self):
        self.assertTemplateUsed(response=self.response, template_name='djaloha/aloha_init.js')

    def test_should_use_default_version_template(self):
        self.assertTemplateUsed(response=self.response, template_name='djaloha/aloha_aloha.0.20.20_init.js')

    def test_should_use_custom_version_init_template(self):
        aloha_version = 'aloha.0.22.1'

        with self.settings(DJALOHA_ALOHA_VERSION=aloha_version):
            response = self.client.get(self.url)
            self.assertTemplateUsed(response=response, template_name='djaloha/aloha_aloha.0.22.1_init.js')

    def test_should_render_jquery_no_conflict(self):
        with self.settings(DJALOHA_JQUERY_NO_CONFLICT=True):
            response = self.client.get(self.url)
            self.assertContains(response, 'jQuery: $.noConflict(true),', count=1, status_code=200)

    def test_should_not_render_jquery_no_conflict_without_config(self):
        with self.settings(DJALOHA_JQUERY_NO_CONFLICT=False):
            response = self.client.get(self.url)
            self.assertContains(response, 'jQuery: $.noConflict(true),', count=0, status_code=200)

    def test_should_not_render_jquery_no_conflict_without_config(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'jQuery: $.noConflict(true),', count=0, status_code=200)

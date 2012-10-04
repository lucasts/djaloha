
from django.test import TestCase
import re
from djaloha.widgets import AlohaInput
from django.conf import settings

ALOHA_JS_MATCH = re.compile(r'src="/static/(.*)/lib/aloha\.js"')
ALOHA_CSS_MATCH = re.compile(r'href="/static/(.*)/css/aloha\.css"')


class MediaPathTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.widget = AlohaInput()

    def tearDown(self):
        try:
            del settings.DJALOHA_ALOHA_VERSION
        except AttributeError:
            pass

    def _assertHasMediaForVersion(self, content, version, regex, message):
        for tags in content:
            matched_src = regex.search(tags)
            if matched_src:
                self.assertEquals(version, matched_src.groups()[0])
                return

        self.fail(message)

    def assertHasCssForVersion(self, content, version, message):
        self._assertHasMediaForVersion(content, version, ALOHA_CSS_MATCH,
                                       message)

    def assertHasJsForVersion(self, content, version, message):
        self._assertHasMediaForVersion(content, version, ALOHA_JS_MATCH,
                                       message)

    def test_aloha_js_path_must_include_aloha_version_number_from_settings(self):
        aloha_version = 'aloha.0.22.1'
        with self.settings(DJALOHA_ALOHA_VERSION=aloha_version):
            content = self.widget.media.render_js()
            self.assertHasJsForVersion(
                content, aloha_version,
                "A path to the Aloha javascript file wasn't found.")

    def test_aloha_css_path_must_include_aloha_version_number_from_settings(self):
        aloha_version = 'aloha.0.22.1'
        with self.settings(DJALOHA_ALOHA_VERSION=aloha_version):
            content = self.widget.media.render_css()
            self.assertHasCssForVersion(
                content, aloha_version,
                "A path to the Aloha css file wasn't found.")

    def test_default_css_path_must_be_use_aloha_0_20_20_version(self):
        aloha_version = 'aloha.0.20.20'
        content = self.widget.media.render_css()
        self.assertHasCssForVersion(
            content, aloha_version,
            "A path to the Aloha css file wasn't found.")

    def test_default_js_path_must_be_use_aloha_0_20_20_version(self):
        aloha_version = 'aloha.0.20.20'
        content = self.widget.media.render_js()
        self.assertHasJsForVersion(
            content, aloha_version,
            "A path to the Aloha css file wasn't found.")

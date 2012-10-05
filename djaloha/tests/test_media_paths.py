
from django.test import TestCase
import re
from djaloha.widgets import AlohaInput
from django.conf import settings

REQUIRE_JS_MATCH = re.compile(r'src="/static/(.*)/lib/require\.js"')
ALOHA_JS_MATCH = re.compile(r'src="/static/(.*)/lib/aloha\.js"')
ALOHA_CSS_MATCH = re.compile(r'href="/static/(.*)/css/aloha\.css"')


class WidgetMediaTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.widget = AlohaInput()

    def assertHasMediaForVersion(self, content, version, regex, message):
        for tags in content:
            matched_src = regex.search(tags)
            if matched_src:
                self.assertEquals(version, matched_src.groups()[0])
                return

        self.fail(message)

    def assertHasCssForVersion(self, content, version, message):
        self.assertHasMediaForVersion(content, version, ALOHA_CSS_MATCH,
                                      message)

    def assertHasJsForVersion(self, content, version, message):
        self.assertHasMediaForVersion(content, version, ALOHA_JS_MATCH,
                                      message)

    def test_should_include_js_for_custom_version(self):
        aloha_version = 'aloha.0.22.1'
        with self.settings(DJALOHA_ALOHA_VERSION=aloha_version):
            content = self.widget.media.render_js()
            self.assertHasJsForVersion(
                content, aloha_version,
                "The Aloha javascript file wasn't found.")

    def test_should_include_css_for_custom_version(self):
        aloha_version = 'aloha.0.22.1'
        with self.settings(DJALOHA_ALOHA_VERSION=aloha_version):
            content = self.widget.media.render_css()
            self.assertHasCssForVersion(
                content, aloha_version,
                "The Aloha css file wasn't found.")

    def test_should_include_require_js_for_newer_versions(self):
        aloha_version = 'aloha.0.22.1'
        with self.settings(DJALOHA_ALOHA_VERSION=aloha_version):
            content = self.widget.media.render_js()
            self.assertHasMediaForVersion(content, aloha_version,
                                          REQUIRE_JS_MATCH,
                                          "require.js wasn't found.")

    def test_should_include_default_version_js(self):
        aloha_version = 'aloha.0.20.20'
        content = self.widget.media.render_css()
        self.assertHasCssForVersion(
            content, aloha_version,
            "A path to the Aloha css file wasn't found.")

    def test_should_include_default_version_css(self):
        aloha_version = 'aloha.0.20.20'
        content = self.widget.media.render_js()
        self.assertHasJsForVersion(
            content, aloha_version,
            "A path to the Aloha css file wasn't found.")

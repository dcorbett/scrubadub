import unittest

import scrubadub

from tests.base import BaseTestCase


class UrlTestCase(unittest.TestCase, BaseTestCase):

    def test_http(self):
        """
        BEFORE: http://bit.ly/aser is neat
        AFTER:  {{URL}} is neat
        """
        self.compare_before_after()

    def test_https(self):
        """
        BEFORE: https://bit.ly/aser is neat
        AFTER:  {{URL}} is neat
        """
        self.compare_before_after()

    def test_www(self):
        """
        BEFORE: www.bit.ly/aser is neat
        AFTER:  {{URL}} is neat
        """
        self.compare_before_after()


    def test_long_url(self):
        """
        BEFORE: https://this.is/a/long?url=very#url is good
        AFTER:  {{URL}} is good
        """
        self.compare_before_after()

    def test_two_urls(self):
        """
        BEFORE: http://bit.ly/number-one http://www.google.com/two
        AFTER:  {{URL}} {{URL}}
        """
        self.compare_before_after()


class UrlKeepDomainTestCase(unittest.TestCase, BaseTestCase):

    def setUp(self):
        scrubadub.filth.UrlFilth.keep_domain = True
        scrubadub.filth.UrlFilth.url_placeholder = 'path/to/something'
        scrubadub.filth.UrlFilth.prefix = ''
        scrubadub.filth.UrlFilth.suffix = ''
        super(UrlKeepDomainTestCase, self).setUp()

    def tearDown(self):
        scrubadub.filth.UrlFilth.keep_domain = False
        scrubadub.filth.UrlFilth.url_placeholder = 'URL'
        scrubadub.filth.UrlFilth.prefix = '{{'
        scrubadub.filth.UrlFilth.suffix = '}}'

    def test_path_word_in_sentence(self):
        """
        BEFORE: Find jobs at http://facebook.com/jobs
        AFTER:  Find jobs at http://facebook.com/path/to/something
        """
        self.compare_before_after()

    def test_keep_domain(self):
        """
        BEFORE: http://public.com/this/is/very/private
        AFTER:  http://public.com/path/to/something
        """
        self.compare_before_after()

    def test_keep_domain_empty_path(self):
        """
        BEFORE: http://public.com/
        AFTER:  http://public.com/path/to/something
        """
        self.compare_before_after()

import unittest

from base import BaseTestCase

from scrubadub.detectors.email import EmailDetector as Detector

class EmailTestCase(unittest.TestCase, BaseTestCase):

    def test_gmail_john(self):
        """
        BEFORE: My email is john@gmail.com
        AFTER:  My email is {{EMAIL}}
        """
        self.compare_before_after()

    def test_fancy_gmail_john(self):
        """
        BEFORE: My email is john at gmail.com
        AFTER:  My email is {{EMAIL}}
        """
        self.compare_before_after()

    def test_standard_imei_many(self):
        """
        BEFORE: Lorem testing@gmail.com . ipsum 12343 dolor sit amet, more.testing@gmail.com. consectetur 23423 adipiscing elit
        AFTER: testing@gmail.com,more.testing@gmail.com
        """
        self.validate_detector(Detector)

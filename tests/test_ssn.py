import unittest

from base import BaseTestCase

from scrubadub.detectors.ssn import SSNDetector


class SSNTestCase(unittest.TestCase, BaseTestCase):

    def test_hyphens(self):
        """
        BEFORE: My social security number is 812-80-1276
        AFTER:  My social security number is {{SSN}}
        """
        self.compare_before_after()

    def test_dots(self):
        """
        BEFORE: My social security number is 812.80.1276
        AFTER:  My social security number is {{SSN}}
        """
        self.compare_before_after()

    def test_spaces(self):
        """
        BEFORE: My social security number is 812 80 1276
        AFTER:  My social security number is {{SSN}}
        """
        self.compare_before_after()

    def test_redact(self):
        """
        TEST: 812 80 1276
        VALIDATE:  Lorem ipsum dolor sit amet, 812 80 1276 consectetur adipiscing elit
        """
        self.validate_detector(SSNDetector)

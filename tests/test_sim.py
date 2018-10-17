import unittest

from base import BaseTestCase

from scrubadub.detectors.sim import SIMDetector as Detector


class SIMTestCase(unittest.TestCase, BaseTestCase):

    def test_standard_17_digit_SIM(self):
        """
        BEFORE: Lorem ipsum 12343 dolor sit amet, 8938475692091392832 Citrix Receiver consectetur 23423 adipiscing elit
        AFTER: 8938475692091392832
        """
        self.validate_detector(Detector)

    def test_standard_18_digit_SIM(self):
        """
        BEFORE: Lorem ipsum 12343 dolor sit amet, 8949384837261029384736 Citrix Receiver consectetur 23423 adipiscing elit
        AFTER: 8949384837261029384736
        """
        self.validate_detector(Detector)

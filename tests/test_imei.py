import unittest

from base import BaseTestCase

from scrubadub.detectors.imei import IMEIDetector as Detector

#https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity

class IMEITestCase(unittest.TestCase, BaseTestCase):

    def test_standard_imei(self):
        """
        BEFORE: Lorem ipsum 12343 dolor sit amet, 867979020438419 Citrix Receiver consectetur 23423 adipiscing elit
        AFTER: 867979020438419
        """
        self.validate_detector(Detector)

    def test_standard_imei_many(self):
        """
        BEFORE: Lorem 520886337211232 ipsum 12343 dolor sit amet, 867979020438419 consectetur 23423 adipiscing elit
        AFTER: 520886337211232,867979020438419
        """
        self.validate_detector(Detector)

    def test_13_digit_imei_(self):
        """
        BEFORE: Lorem 3948723648309 ipsum 12343 dolor sit amet, 867979020438419 consectetur 23423 adipiscing elit
        AFTER: 3948723648309,867979020438419
        """
        self.validate_detector(Detector)


import unittest

from base import BaseTestCase

from scrubadub.detectors.mac_address import MacAddressDetector as Detector

#https://en.wikipedia.org/wiki/MAC_address#Address_details

class IMEITestCase(unittest.TestCase, BaseTestCase):

    def test_standard(self):
        """
        BEFORE: Lorem ipsum 12343 dolor sit amet, 00-D0-56-F2-B5-12  consectetur 23423 adipiscing elit
        AFTER: 00-D0-56-F2-B5-12
        """
        self.validate_detector(Detector)

    def test_standard_many(self):
        """
        BEFORE: Lorem  00-26-DD-14-C4-EE ipsum 12343 dolor sit amet, 00-D0-56-F2-B5-12  consectetur 23423 adipiscing elit
        AFTER:  00-26-DD-14-C4-EE,00-D0-56-F2-B5-12
        """
        self.validate_detector(Detector)


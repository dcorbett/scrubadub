import unittest

from base import BaseTestCase

from scrubadub.detectors.ipv4_address import Ipv4AddressDetector as Detector

#https://en.wikipedia.org/wiki/IP_address#IPv4_addresses

class Ipv4AddressTestCase(unittest.TestCase, BaseTestCase):

    def test_standard(self):
        """
        BEFORE: Lorem ipsum 12343 dolor sit amet, 127.255.255.255 consectetur 23423 adipiscing elit
        AFTER: 127.255.255.255
        """
        self.validate_detector(Detector)

    def test_standard_many(self):
        """
        BEFORE: Lorem 172.31.255.255 ipsum 12343 dolor sit amet, 127.255.255.255 consectetur 23423 adipiscing elit
        AFTER: 172.31.255.255,127.255.255.255
        """
        self.validate_detector(Detector)


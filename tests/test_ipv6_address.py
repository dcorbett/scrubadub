import unittest

from base import BaseTestCase

from scrubadub.detectors.ipv6_address import Ipv6AddressDetector as Detector

#https://en.wikipedia.org/wiki/IPv6#Motivation_and_origin

class Ipv6AddressTestCase(unittest.TestCase, BaseTestCase):

    def test_standard(self):
        """
        BEFORE: Lorem ipsum 12343 dolor sit amet, 6c48:359c:d17c:53a7:dbed:4491:bcd7:c7f9 consectetur 23423 adipiscing elit
        AFTER: 6c48:359c:d17c:53a7:dbed:4491:bcd7:c7f9
        """
        self.validate_detector(Detector)

    def test_standard_many(self):
        """
        BEFORE: Lorem 76a5:7b1a:c638:2390:b2fb:5a02:b976:58ac ipsum 12343 dolor sit amet, 3ee3:e8e9:b6dc:f01a:23ce:40c6:39e0:7d6 consectetur 23423 adipiscing elit
        AFTER: 76a5:7b1a:c638:2390:b2fb:5a02:b976:58ac,3ee3:e8e9:b6dc:f01a:23ce:40c6:39e0:7d6
        """
        self.validate_detector(Detector)


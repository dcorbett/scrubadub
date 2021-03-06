import unittest

from base import BaseTestCase

from scrubadub.detectors.phone_alt import PhoneAltDetector as Detector


class PhoneNumberTestCase(unittest.TestCase, BaseTestCase):

    def create_docstring(self, phone_number):
        return """
        BEFORE: My phone number is %s
        AFTER:  My phone number is {{PHONE}}
        """ % phone_number

    def create_docstring_neutral(self, phone_number):
        return """
        BEFORE: My phone number is %s
        AFTER:  My phone number is %s
        """ % (phone_number, phone_number)

    def check_phone_numbers(self, *phone_numbers):
        for phone_number in phone_numbers:
            self.compare_before_after(
                docstring=self.create_docstring(phone_number),
            )

    def ensure_phone_number_neutral(self, *phone_numbers):
        for phone_number in phone_numbers:
            self.compare_before_after(
                docstring=self.create_docstring_neutral(phone_number),
            )

    def test_american_phone_number(self):
        """test american-style phone numbers"""
        self.check_phone_numbers(
            '1-312-515-2239',
            '+1-312-515-2239',
            '1 (312) 515-2239',
            '312-515-2239',
            '(312) 515-2239',
            '(312)515-2239',
        )

    def test_extension_phone_numbers(self):
        """test phone numbers with extensions"""
        self.check_phone_numbers(
            '312-515-2239 x12',
            '312-515-2239 ext. 12',
            '312-515-2239 ext.12',
        )

    def test_international_phone_numbers(self):
        """test international phone numbers"""
        self.check_phone_numbers(
            '+47 21 30 85 99',
            '+45 69 19 88 56',
            '+46 852 503 499',
            '+31 619 837 236',
            '+86 135 3727 4136',
            '+61267881324',
        )

    def test_multiple_phone_numbers(self):
        # running this through scrubadub.clean replaces 'reached at
        # 312.714.8142' with '{{EMAIL}}'. See issue
        result = self.clean(
            u'Call me on my cell 312.714.8142 or in my office 773.415.7432'
        )
        self.assertEqual(
            result,
            u'Call me on my cell {{PHONE}} or in my office {{PHONE}}',
            'problem with multiple phone numbers: \n %s' % result,
        )

    def test_standard_wText(self):
        """
        BEFORE: Lorem ipsum 12343 dolor sit amet, US4052034739 consectetur 23423 adipiscing elit
        AFTER: US4052034739
        """
        self.validate_detector(Detector)

    def test_hotline_numbers(self):
        self.ensure_phone_number_neutral(
            '18005883600',
            '1-800-588-3600',
            '1 (800) 515-2239',
            '900.515-2239',
            '(888) 515-2239',
            '(800)515-2239',
        )

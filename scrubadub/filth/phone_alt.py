import re

from .base import RegexFilth


class PhoneAltFilth(RegexFilth):
    type = 'phone_alt'

    # This identifies Phone numbers that are outliers but must be handled
    regex = re.compile((
        "[A-Z]{2}\d{10}(?=\s)"
    ), re.VERBOSE)

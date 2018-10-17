import re

from .base import RegexFilth


class IMEIFilth(RegexFilth):
    type = 'imei'

    # This caputures International Mobile Equipment Indentity numbers
    # This captures valid and possibly invalid numbers
    # Check sum validation is not preformed.
    # Alternative versions are not preformed
    # A check is only made on the structure
    # https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity
    # A check sum step is required
    # there are 2 versions. This only checks the 
    # ^(?!\b(.)\1+\b)\d{15}$ 
    regex = re.compile((
        "\d{13,15}"       # imei number is a 15 digit number. Lowering this to 13 to catch all
    ), re.VERBOSE)

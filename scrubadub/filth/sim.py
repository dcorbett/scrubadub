import re

from .base import RegexFilth


class SIMFilth(RegexFilth):
    type = 'sim'

    #This will only redact Issuer identification number.
    # https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID
    regex = re.compile((
        "89\d{17,20}"
    ), re.VERBOSE)

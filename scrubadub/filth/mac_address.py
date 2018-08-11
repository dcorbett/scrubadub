import re

from .base import RegexFilth


class MacAddressFilth(RegexFilth):
    type = 'mac_address'

    # This identifies the mac address in a line of text
    # https://en.wikipedia.org/wiki/MAC_address
    # ([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})
    regex = re.compile((
        "([0-9A-Fa-f]{2}[:-]){5}"       # 5 instances of two alpha pairs seperated by colons
        "([0-9A-Fa-f]{2})"              # a final alphanumeric value
    ), re.VERBOSE)

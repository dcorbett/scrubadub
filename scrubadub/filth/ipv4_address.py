import re

from .base import RegexFilth


class Ipv4AddressFilth(RegexFilth):
    type = 'ipv4_address'

    # This caputures IP addresses
    # This captures valid IP addresses v4
    # https://en.wikipedia.org/wiki/IPv4#Addressing
    # ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$
    regex = re.compile((
        "(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}"
        "([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    ), re.VERBOSE)

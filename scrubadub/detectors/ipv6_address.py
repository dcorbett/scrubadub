import re

from .base import RegexDetector
from ..filth import Ipv6AddressFilth


class Ipv6AddressDetector(RegexDetector):
    """Use regular expression magic to identify IPv6 values
    https://en.wikipedia.org/wiki/IPv6#Motivation_and_origin
    """

    filth_cls = Ipv6AddressFilth

import re

from .base import RegexDetector
from ..filth import Ipv4AddressFilth


class Ipv4AddressDetector(RegexDetector):
    """Use regular expression magic to identify IMEI values
    https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity
    """

    filth_cls = Ipv4AddressFilth

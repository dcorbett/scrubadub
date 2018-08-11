import re

from .base import RegexDetector
from ..filth import MacAddressFilth


class MacAddressDetector(RegexDetector):
    """Use regular expression magic to identify Mac Address values
    https://en.wikipedia.org/wiki/MAC_address
    """

    filth_cls = MacAddressFilth
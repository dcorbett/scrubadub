import re

from .base import RegexDetector
from ..filth import IMEIFilth


class IMEIDetector(RegexDetector):
    """Use regular expression magic to identify IMEI values
    https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity
    """

    filth_cls = IMEIFilth

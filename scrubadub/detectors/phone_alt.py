import re

from .base import RegexDetector
from ..filth import PhoneAltFilth


class PhoneAltDetector(RegexDetector):
    """This Class is used to handle the alternate version of phone numbers
    """

    filth_cls = PhoneAltFilth
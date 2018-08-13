
# convenient imports
from .scrubbers import Scrubber
from . import filth
from . import detectors

__version__ = VERSION = "1.2.0"


def clean(text, cls=None, **kwargs):
    """Public facing function to clean ``text`` using the scrubber ``cls`` by
    replacing all personal information with ``{{PLACEHOLDERS}}``.
    """
    cls = cls or Scrubber
    scrubber = cls()
    return scrubber.clean(text, **kwargs)

def find_sensitive(text, cls=None):
    #Public facing function to locate sensitive data
    #It returns a list of locations and the word located
    cls = cls or Scrubber
    scrubber = cls()
    return scrubber.find_sensitive(text)

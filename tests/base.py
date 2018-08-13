import inspect

import scrubadub


try:
    unicode
except NameError:
    unicode = str  # Python 2 and 3 compatibility

# this is a mixin class to make it easy to centralize a lot of the core
# functionality of the test suite
class BaseTestCase(object):

    def clean(self, text, **kwargs):
        if 'replace_with' in kwargs:
            scrubadub.filth.base.Filth.lookup = scrubadub.utils.Lookup()
        return scrubadub.clean(text, **kwargs)

    def find_sensitive(self, text):
        return scrubadub.find_sensitive(text)

    def get_before_after(self, docstring=None, before="BEFORE:", after="AFTER:"):
        """Recursively parse the docstrings of methods that are called in the
        stack to find the docstring that has been used to define the test.
        """
        # get the before and after outcomes from the docstring of the method
        # that calls compare_before_after
        if docstring is None:
            stack = inspect.stack()
            for frame in inspect.stack():
                calling_function_name = frame[3]
                _docstring = getattr(self, calling_function_name).__doc__
                if before in _docstring and after in _docstring:
                    docstring = _docstring
                    break
        before, after = docstring.split(before)[1].split(after)
        return unicode(before.strip()), unicode(after.strip())

    def check_equal(self, expected, actual):
        """This method makes it easy to give useful error messages when running
        nosetests
        """
        self.assertEqual(
            actual,
            expected,
            '\nEXPECTED:\n"%s"\n\nBUT GOT THIS:\n"%s"'%(expected, actual),
        )

    def compare_before_after(self, docstring=None, **clean_kwargs):
        """Convenience method for quickly writing tests using the BEFORE and
        AFTER keywords to parse the docstring.
        """
        before, after = self.get_before_after(docstring=docstring)
        self.check_equal(after, self.clean(before, **clean_kwargs))

    def validate_detector(self, detector, docstring=None ):
        """Convenience method for quickly writing tests using the BEFORE and
        AFTER keywords to parse the docstring. This is specifically for the redact
        """
        before, after = self.get_before_after(docstring=docstring, before="TEST:", after="VALIDATE:")

        result_set = []
        for next_filth in detector.iter_filth(detector(),after):
            result_set.append(next_filth.text)
        self.check_equal(len(result_set), 1)
        self.check_equal(before, result_set[0])


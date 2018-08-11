
.. NOTES FOR CREATING A RELEASE:
..
..   * bump the version number
..   * update docs/changelog.rst
..   * git push
..   * python setup.py sdist upload
..   * create a release https://github.com/datascopeanalytics/scrubadub/releases


scrubadub
=========

Below is an example of the extend find sensitve feature. The example below returns a list of redact objects that will contain sensitve informatino. The first redact object will contain ``type:email text:alice@example.com start:8 end:25`` The start and the end are the length of the word + 1. 

    import scrubadub

    scrubber = scrubadub.Scrubber()

    text = """
    Email: alice@example.com 
    IMEI: 109447782633260
    MAC Address: 00-14-22-01-23-45
    IPv4: 255.255.255.2
    """
    text = unicode(text, "utf-8")
    redact_list = scrubber.find_sensitive(text)

    for redact in redact_list:
        print(redact)

    print(text)

*please note Not all text need to be converted to unicode, this will eventaully be removed.

`Full documentation <http://scrubadub.readthedocs.org>`__.

|Build Status| |Version| |Downloads| |Test Coverage| |Documentation Status|

.. |Build Status| image:: https://travis-ci.org/datascopeanalytics/scrubadub.svg?branch=master
   :target: https://travis-ci.org/datascopeanalytics/scrubadub
.. |Version| image:: https://pypip.in/v/scrubadub/badge.png
   :target: https://warehouse.python.org/project/scrubadub/
.. |Downloads| image:: https://pypip.in/d/scrubadub/badge.png
   :target: https://warehouse.python.org/project/scrubadub/
.. |Test Coverage| image:: https://coveralls.io/repos/datascopeanalytics/scrubadub/badge.png
   :target: https://coveralls.io/r/datascopeanalytics/scrubadub
.. |Documentation Status| image:: https://readthedocs.org/projects/scrubadub/badge/?version=latest
   :target: https://readthedocs.org/projects/scrubadub/?badge=latest

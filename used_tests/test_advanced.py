import unittest

from base import BaseTestCase


class AdvancedTestCase(unittest.TestCase, BaseTestCase):

    @unittest.skip("Custom Native Test - detector unused")
    def test_disable_email(self):
        """
        BEFORE: contact Joe Duffy at joe@example.com
        AFTER:  contact {{NAME}} {{NAME}} at joe@example.com
        """
        before, after = self.get_before_after()
        import scrubadub
        scrubber = scrubadub.Scrubber()
        scrubber.remove_detector('email')
        self.check_equal(after, scrubber.clean(before))

    @unittest.skip("Custom Native Test - detector unused")
    def test_customize_filth_identification(self):
        """
        BEFORE: contact Joe Duffy at joe@example.com
        AFTER:  contact <b>NAME</b> <b>NAME</b> at <b>EMAIL</b>
        """
        before, after = self.get_before_after()
        import scrubadub
        prefix = scrubadub.filth.base.Filth.prefix
        suffix = scrubadub.filth.base.Filth.suffix
        scrubadub.filth.base.Filth.prefix = u'<b>'
        scrubadub.filth.base.Filth.suffix = u'</b>'
        scrubber = scrubadub.Scrubber()
        self.check_equal(after, scrubber.clean(before))
        scrubadub.filth.base.Filth.prefix = prefix
        scrubadub.filth.base.Filth.suffix = suffix

    @unittest.skip("Custom Native Test - detector unused")
    def test_identifier(self):
        """
        BEFORE: i'm on skype (dean.malmgren) or can be reached at +1.800.346.1819
        AFTER:  i'm on skype ({{SKYPE-0}}) or can be reached at {{PHONE-1}}
        """
        self.compare_before_after(replace_with='identifier')

    @unittest.skip("Custom Native Test - detector unused")
    def test_identifier_repeat(self):
        """
        BEFORE: my name is Dean Malmgren. Did I mention my name is Dean?
        AFTER:  my name is {{NAME-0}} {{NAME-1}}. Did I mention my name is {{NAME-0}}?
        """
        self.compare_before_after(replace_with='identifier')

"""
Unit testing the check() method of the validate email module.
"""
import unittest
import validate_email

class TestDateDiff(unittest.TestCase):
    """
        Includes test case for validating the email ID's check() method of validate_email module
    """
    def test_valid_email(self):
        """
            Email ID's as per the guidelines
        """
        eid1 = 'username@domainname.ext'
        eid2 = 'user24name@domainname.ext'
        eid3 = 'user_name@domainname.ext'
        self.assertTrue(validate_email.check(eid1))
        self.assertTrue(validate_email.check(eid2))
        self.assertTrue(validate_email.check(eid3))

    def test_invalid_email_website(self):
        """
        Alphanumeric website name. Website name can only have letters and digits.
        """
        eid = 'A.lakmale@gma_il.com'
        self.assertFalse(validate_email.check(eid))

    def test_invalid_email_extension(self):
        """
         The maximum length of the extension is 3
        """
        eid = 'username24@hypen_included.moreThanThreeLetters'
        self.assertFalse(validate_email.check(eid))

    def test_invalid_email_special_char(self):
        """
        Special characters in username
        """
        eid = 'username#$24@gmail.com'
        self.assertFalse(validate_email.check(eid))

    def test_empty_email(self):
        """
            Empty email ID
        """
        eid = ''
        self.assertFalse(validate_email.check(eid))

if __name__ == '__main__':
    unittest.main()

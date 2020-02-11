"""
Unit testing the solution function for the date difference module.
"""
import unittest
import date_diffrence

class TestDateDiff(unittest.TestCase):
    """
    Includes test case for validating the solution() method of date_diffrence module
    """
    def test_date_diff(self):
        """
            Valid timestamps
        """
        time_1 = 'Sun 10 May 2015 13:54:36 -0700'
        time_2 = 'Sun 10 May 2015 13:54:36 -0000'
        time_3 = 'Sat 02 May 2015 19:54:36 +0530'
        time_4 = 'Fri 01 May 2015 13:54:36 -0000'
        self.assertEqual(date_diffrence.solution(time_1, time_2), 25200)
        self.assertEqual(date_diffrence.solution(time_3, time_4), 88200)

    def test_invalid_year(self):
        """
            Invalid Year
        """
        time_1 = 'Sun 10 May 2015 13:54:36 -0000'
        time_2 = 'Sun 10 May 3001 13:54:36 -0000'
        self.assertEqual(date_diffrence.solution(time_1, time_2), 'Invalid Year!')

    def test_invalid_timestap(self):
        """
            Invalid Timestamp
        """
        time_1 = '2012-11-14 16:24:18.071000'
        time_2 = 'Sun 10 May 3001 13:54:36 -0000'
        self.assertEqual(date_diffrence.solution(time_1, time_2), 'Invalid Timestamp!')

    def test_empty_timestap(self):
        """
            Invalid Timestamp (Empty)
        """
        time_1 = ''
        time_2 = 'Sun 10 May 3001 13:54:36 -0000'
        self.assertEqual(date_diffrence.solution(time_1, time_2), 'Invalid Timestamp!')

if __name__ == '__main__':
    unittest.main()

import unittest

from year import Year


class YearTest(unittest.TestCase):
    """
    A year is not a leap year if not divisible by 4
    A year is a leap year if divisible by 4
    A year is a leap year if divisible by 400
    A year is not a leap year if divisible by 100 but not by 400
    """

    def test_not_leap_year_if_not_divisible_by_4(self):
        year = Year(1997)
        self.assertFalse(year.is_leap())

    def test_is_leap_year_if_divisible_by_4(self):
        year = Year(1996)
        self.assertTrue(year.is_leap())

    def test_is_leap_year_if_divisible_by_400(self):
        year = Year(1600)
        self.assertTrue(year.is_leap())

    def test_not_leap_year_if_divisible_by_100_but_not_by_400(self):
        year = Year(1900)
        self.assertFalse(year.is_leap())


if __name__ == '__main__':
    unittest.main()

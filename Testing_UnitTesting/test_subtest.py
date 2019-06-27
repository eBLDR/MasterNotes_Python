import unittest


class NumbersTest(unittest.TestCase):

    def setUp(self):
        self.numbers = range(1, 6)

    def test_even(self):
        # Test if all numbers are even
        for number in self.numbers:
            # Using a subTest, allows execution to continue, displaying
            # normally the result of the subTest as any other test
            # The parameters passed to subTest will be displayed in the output,
            # just for info
            with self.subTest(number=number):
                self.assertEqual(number % 2, 0)


if __name__ == '__main__':
    unittest.main()

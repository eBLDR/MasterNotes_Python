"""
Test fixtures are resources needed by a test.
"""
import unittest


class FixturesTest(unittest.TestCase):

    def setUp(self):
        # This special method is always called prior to every single test,
        # to configure fixtures
        print('In setUP()')
        self.fixture = range(1, 10)  # Can be any resource

    def tearDown(self):
        # This special method is always called at the end of every single test,
        # to clean up fixtures
        print('In tearDown()')
        # It's good to delete all fixtures, to avoid memory problems
        del self.fixture

    def test_1(self):
        print('In test_1()')
        self.assertEqual(self.fixture, range(1, 10))

    def test_2(self):
        print('In test_2()')
        self.assertIn(5, self.fixture)


if __name__ == '__main__':
    unittest.main()

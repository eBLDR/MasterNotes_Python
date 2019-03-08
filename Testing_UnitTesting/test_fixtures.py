"""
Test fixtures are resources needed by a test.
"""
import unittest


class FixturesTest(unittest.TestCase):

    def setUp(self):
        # This special method is always called first, to configure fixtures
        print('In setUP()')
        self.fixture = range(1, 10)  # Can be any resource

    def tearDown(self):
        # This special method is always called last, to clean up fixtures
        print('In tearDown()')
        del self.fixture

    def test(self):
        print('In test()')
        self.assertEqual(self.fixture, range(1, 10))


if __name__ == '__main__':
    unittest.main()

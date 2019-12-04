"""
Automated testing framework, unittest, sometimes referred to as 'PyUnit'.
Each test written must be fully independent, able to run alone, it should
focus on one bit of functionality.
"""
import unittest


# Class must inherit from unittest.TestCase
class OutcomesTest(unittest.TestCase):

    # Method's names must start with 'test'
    def test_pass(self):
        # Outcome will be 'ok'
        self.assertTrue(True)

    def test_fail(self):
        # Outcome will be 'FAIL'
        self.assertFalse(True, msg='Customised fail/error msg')

    def test_error(self):
        # Outcome will be 'ERROR'
        raise RuntimeError('Test error!')

    # Decorator for skipping a test, outcome will be 'skipped'
    @unittest.skip('I am being skipped just because')
    def test_skip_me(self):
        pass

    """
    @skipIf(condition, reason) decorator will skip the test
    if condition isTrue
    @skipUnless(condition, reason) decorator will skip a test
    unless the condition is True
    """

    # If failure is expected, use @unittest.expectedFailure decorator
    # if the test fails it will be considered a success, and failed if ti passes
    @unittest.expectedFailure
    def test_i_am_a_failure(self):
        self.assertEqual(1, 2)


# This is not necessary if running from terminal
if __name__ == '__main__':
    unittest.main()

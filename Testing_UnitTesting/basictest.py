"""
Automated testing framework, unittest, sometimes referred to as 'PyUnit'.
Each test written must be fully independent, able to run alone, it should
focus on one bit of functionality.
To run the test from cmd, add -v (verbose) option to display extra information.

There are 3 possible outcomes:
    - ok (.) -> test passed
    - FAIL (F) -> test failed, raises and AssertionError exception
    - ERROR (E) -> raises an exception other than AssertionError
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
    @skipIf(condition, reason) decorator will skip the test if condition is True
    @skipUnless(condition, reason) decorator will skip a test unless the condition is True
    """


if __name__ == '__main__':
    unittest.main()

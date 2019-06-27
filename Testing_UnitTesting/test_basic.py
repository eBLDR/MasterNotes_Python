"""
Automated testing framework, unittest, sometimes referred to as 'PyUnit'.
Each test written must be fully independent, able to run alone, it should
focus on one bit of functionality.

To run the test from cmd use:

$ python -m unittest <module_name>

The above line will run all files that sta
Add -v (verbose) flag to display extra output.

To run in discover mode, this will search for all the files with a name
starting with 'test' and run them:

$ python -m unittest

To list all unittest options use:

$ python -m unittest -h

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

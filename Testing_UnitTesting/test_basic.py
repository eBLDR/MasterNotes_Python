"""
Automated testing framework, unittest, sometimes referred to as 'PyUnit'.
Each test written must be fully independent, able to run alone, it should
focus on one bit of functionality.
unittest will run the tests inside the test case in alphabetical order.
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

    # Using built-in assert for custom assert expressions
    def test_with_keyword_assert(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"


# Following is not necessary if the test file is run directly (instead of
# invoking it through a test runner)
if __name__ == '__main__':
    unittest.main()

import unittest


class AssertionMethods(unittest.TestCase):

    # Common assertions
    def test_true(self):
        self.assertTrue(0 < 1)

    def test_false(self):
        self.assertFalse(1 < 1)

    def test_is_none(self):
        self.assertIsNone(None)

    def test_is_not_none(self):
        self.assertIsNotNone(1)

    def test_equal(self):
        self.assertEqual(1, 1)  # a == b should return True

    def test_not_equal(self):
        self.assertNotEqual(0, 1)  # a != b should return True

    def test_is(self):
        self.assertIs(1, 1)  # a is b should return True

    def test_is_not(self):
        self.assertIsNot(0, 1)  # a is not b should return True

    def test_in(self):
        self.assertIn(0, [0])  # a in b should return True

    def test_not_in(self):
        self.assertNotIn(0, [1])  # a not in b should return True

    # Other assertions
    """
    assertIsInstance(a, b, msg=None)
    assertNotIsInstance(a, b, msg=None)
    assertAlmostEqual(a, b, places=7, msg=None, delta=None)
    assertNotAlmostEqual(a, b, places=7, msg=None, delta=None)
    assertGreater(a, b, msg=None)
    assertGreaterEqual(a, b, msg=None)
    assertLess(a, b, msg=None)
    assertLessEqual(a, b, msg=None)
    assertRegex(text, regexp, msg=None)
    assertNotRegex(text, regexp, msg=None)
    assertCountEqual(a, b, msg=None)
    assertMultiLineEqual(a, b, msg=None)
    assertSequenceEqual(a, b, msg=None)
    assertListEqual(a, b, msg=None)
    assertTupleEqual(a, b, msg=None)
    assertSetEqual(a, b, msg=None)
    assertDictEqual(a, b, msg=None)
    
    # Asserting exceptions
    assertRaises(exception)
    assertRaisesRegex(exception, regexp)
    assertWarns(warn, fun, *args, **kwds)
    assertWarnsRegex(warn, fun, *args, **kwds)
    """

    
if __name__ == '__main__':
    unittest.main()

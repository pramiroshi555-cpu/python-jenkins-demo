import unittest
from condition import check_even, check_odd


class TestCondition(unittest.TestCase):

    def test_even(self):
        self.assertTrue(check_even(10))

    def test_odd(self):
        self.assertTrue(check_odd(5))


if __name__ == "__main__":
    unittest.main()
import unittest
import sys
 
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime_non_integer_numbers(self):
        self.assertIsNone(is_prime(2.5))
        self.assertIsNone(is_prime(43.14))
        self.assertIsNone(is_prime(90.57))
        self.assertIsNone(is_prime(-4.7))
        self.assertIsNone(is_prime(-36.56))
        self.assertIsNone(is_prime(-85.89))

if __name__ == '__main__':
    unittest.main()

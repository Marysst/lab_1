import unittest
import sys
 
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime_positive_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(23))

if __name__ == '__main__':
    unittest.main()

import unittest
import sys

sys.path.append("..")  
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime_custom_divisor(self):
        self.assertTrue(is_prime(13, 4))
        self.assertFalse(is_prime(15, 4))
        self.assertTrue(is_prime(17, 5))
        self.assertFalse(is_prime(18, 5))
        self.assertTrue(is_prime(23, 7))
        self.assertFalse(is_prime(54, 6))

if __name__ == '__main__':
    unittest.main()

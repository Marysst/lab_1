import unittest
import sys

sys.path.append("..")  
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime_large_numbers(self):
        self.assertFalse(is_prime(17945))
        self.assertTrue(is_prime(38953))
        self.assertFalse(is_prime(50937))
        self.assertTrue(is_prime(63901))
        self.assertTrue(is_prime(81157))
        self.assertFalse(is_prime(94780))

if __name__ == '__main__':
    unittest.main()

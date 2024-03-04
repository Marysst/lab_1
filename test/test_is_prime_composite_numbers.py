import unittest
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(file), os.pardir))

sys.path.insert(0, parent_dir)
 
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
        def test_is_prime_composite_numbers(self):
                self.assertFalse(is_prime(4))
                self.assertFalse(is_prime(12))
                self.assertFalse(is_prime(25))
                self.assertFalse(is_prime(49))
                self.assertFalse(is_prime(93))

if __name__ == '__main__':
    unittest.main()

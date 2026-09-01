# test_cryptoforgediamond.py
"""
Tests for CryptoForgeDiamond module.
"""

import unittest
from cryptoforgediamond import CryptoForgeDiamond

class TestCryptoForgeDiamond(unittest.TestCase):
    """Test cases for CryptoForgeDiamond class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoForgeDiamond()
        self.assertIsInstance(instance, CryptoForgeDiamond)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoForgeDiamond()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

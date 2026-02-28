# test_viewaxion.py
"""
Tests for ViewAxion module.
"""

import unittest
from viewaxion import ViewAxion

class TestViewAxion(unittest.TestCase):
    """Test cases for ViewAxion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ViewAxion()
        self.assertIsInstance(instance, ViewAxion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ViewAxion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_rollupcore.py
"""
Tests for RollupCore module.
"""

import unittest
from rollupcore import RollupCore

class TestRollupCore(unittest.TestCase):
    """Test cases for RollupCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RollupCore()
        self.assertIsInstance(instance, RollupCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RollupCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

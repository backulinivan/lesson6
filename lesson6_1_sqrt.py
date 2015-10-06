import unittest
import lib

class LibTest(unittest.TestCase):
    
    def test_sqrt_posnums(self):
        self.assertEqual(lib.sqrt(16), 4)
        self.assertEqual(lib.sqrt(1), 1)
        self.assertEqual(lib.sqrt(0), 0)
    
    def test_sqrt_negnums(self):
        self.assertEqual(lib.sqrt(-1), 0)
        
unittest.main(verbosity=2)               

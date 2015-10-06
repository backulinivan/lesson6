import unittest
import lib

class LibTest(unittest.TestCase):

    def test_pos_nums(self):
        self.assertEqual(lib.factorial(0), 1)
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(5), 120)
    
    def test_neg_nums(self):
        self.assertNotEqual(lib.factorial(-1), -1)
        self.assertNotEqual(lib.factorial(-3), -6)
            
unittest.main(verbosity=2)        

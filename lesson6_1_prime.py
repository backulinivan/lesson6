import unittest
import lib

class LibTest(unittest.TestCase):

    def test_pos_nums(self):
        self.assertEqual(lib.prime(1), False)
        self.assertEqual(lib.prime(2), True)
        self.assertEqual(lib.prime(4), False)
        self.assertEqual(lib.prime(11), True)
        
    def test_neg_nums(self):
        self.assertEqual(lib.prime(-3), False)
        
unittest.main(verbosity=2)                

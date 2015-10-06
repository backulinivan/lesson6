import unittest
import lib

class LibTest(unittest.TestCase):

    def test_correct_runtime(self):
        self.assertEqual(lib.even(2), True)
        self.assertEqual(lib.even(0), True)
        self.assertEqual(lib.even(10), True)
        self.assertEqual(lib.even(1), False)
    
    def test_incorrect_runtime(self):
        self.assertEqual(lib.even(3), False)
        self.assertEqual(lib.even(-1), False)
       
unittest.main(verbosity=2)            

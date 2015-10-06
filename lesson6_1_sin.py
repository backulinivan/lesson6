import unittest
import lib
import math

class LibTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(lib.sin(0), 0)
        self.assertEqual(lib.sin(3.1415926), 0)
        self.assertEqual(lib.sin(1.07), math.sin(1.07))
    
    def test_lessthan1(self):
        self.assertLessEqual(lib.sin(1.58), 1)
        self.assertGreaterEqual(lib.sin(-1.58), -1)    

unittest.main(verbosity=2)


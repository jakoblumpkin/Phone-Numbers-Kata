import unittest
from generate_data import random_phonenumber

class TestData(unittest.TestCase):
    
    def testLength(self):
        theLength = len(random_phonenumber())
        self.assertTrue(theLength > 1)
        random_phonenumber()

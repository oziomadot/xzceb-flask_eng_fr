import unittest
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from translator import englishToFrench, frenchToEnglish





class TestE2F(unittest.TestCase): 
    def test(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        
                

class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')   
        
unittest.main()
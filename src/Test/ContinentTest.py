'''
Created on Feb 21, 2013

@author: shengchao
'''
import unittest
from DataParse import Parser
from DataParse import QueryingData

class ContinentTest(unittest.TestCase):
    
    Parser.Parser()
    
    def testHKGinAsia(self):
        key = False
        for city in QueryingData.asia:
            if city == 'Hong Kong':
                key = True
        self.assertEqual(key, True)
        
    def testSCLinSouthAmercia(self):
        key = False
        for city in QueryingData.southAmerica:
            if city == 'Santiago':
                key = True
        self.assertEqual(key, True)
        
    def testMEXinNorthAmerica(self):
        key = False
        for city in QueryingData.northAmerica:
            if city == 'Mexico City':
                key = True
        self.assertEqual(key, True)
        
    def testMADinEurope(self):
        key = False
        for city in QueryingData.europe:
            if city == 'Madrid':
                key = True
        self.assertEqual(key, True)
        
    def testLOSinAfrica(self):
        key = False
        for city in QueryingData.africa:
            if city == 'Lagos':
                key = True
        self.assertEqual(key, True)
            
    
'''
Created on Feb 20, 2013

@author: shengchao
'''

import unittest
from DataParse import Parser
from DataParse import QueryingData

class ParseTest(unittest.TestCase):
    
    Parser.Parser()
    
    def testShanghai(self):
        key = QueryingData.cityDicationary.has_key("Shanghai")
        self.assertEqual(key, True)
        
    def testSHAtoPEKdistance(self):
        key = 0
        for item in QueryingData.routeList:
            if item.takeOffPortCode == 'SHA' and item.landPortCode == 'PEK':
                key = item.distance
        self.assertEqual(key, 1075)
        
    def testPEKpopulation(self):
        key = 0
        beijingInfo = None
        for cityName, cityInfo in QueryingData.cityDicationary.iteritems():
            if cityName == 'Beijing':
                beijingInfo = cityInfo
                break
        self.assertEqual(beijingInfo.population, 13600000)
                
                
    def testSHAtoShanghai(self):
        key = QueryingData.codeToName.has_key("SHA")
        self.assertEqual(key, True)
        
    
        
    
    

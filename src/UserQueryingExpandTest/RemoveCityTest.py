'''
Created on Mar 1, 2013

@author: shengchao
'''

import unittest
from DataParse import Parser
from DataParse import QueryingData
from DataParse import UserQueryingExpand

class QueryTest(unittest.TestCase):
    
    Parser.Parser()
    
    def testRemoveCity(self):
        UserQueryingExpand.removeCity()
        key = 'Champaign'
        self.assertFalse(key in QueryingData.cityDicationary)
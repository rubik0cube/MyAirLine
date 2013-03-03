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
    
    def testAddCity(self):
        UserQueryingExpand.addCity()
        key = 'Hangzhou'
        self.assertTrue(key in QueryingData.continent)
        self.assertTrue(key in QueryingData.cityDicationary)
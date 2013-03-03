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
    
    def testEditCity(self):
        UserQueryingExpand.editCity()
        oldName = "Champaign"
        newName = "Urbana"
        self.assertTrue(newName in QueryingData.cityDicationary)

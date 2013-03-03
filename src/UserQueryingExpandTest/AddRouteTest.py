'''
Created on Mar 1, 2013

@author: shengchao
'''
import unittest
from DataParse import Parser
from DataParse import UserQuerying
from DataParse import UserQueryingExpand

class QueryTest(unittest.TestCase):
    
    Parser.Parser()
    
    def testAddRoute(self):
        UserQueryingExpand.addRoute()
        source = "Champaign"
        dest = "Shanghai"
        self.assertTrue(dest in UserQuerying.getFlyToCity(source))
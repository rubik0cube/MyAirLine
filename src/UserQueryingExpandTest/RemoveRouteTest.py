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
    
    def testRemoveRoute(self):
        UserQueryingExpand.removeRoute()
        source = "Hong Kong"
        dest = "Shanghai"
        self.assertFalse(dest in UserQuerying.getFlyToCity(source))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
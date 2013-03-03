'''
Created on Feb 27, 2013

@author: shengchao
'''
from DataParse import Parser
from DataParse import QueryingData
from DataParse import UserQueryingExpand
from DataParse import UserQuerying
from DataParse import DijkstraAlgorithm

Parser.Parser()

graph = {}
for city in QueryingData.cityDicationary:
    
    graph[city] = UserQuerying.getFlyToCity(city)
    
print DijkstraAlgorithm.shortestPath(graph, "Los Angeles", "London")

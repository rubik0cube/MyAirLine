'''
Created on Feb 20, 2013

@author: shengchao
'''
import json
import urllib2
import QueryingData
import UserQuerying
from MyGraphLib import CityInfo
from MyGraphLib import RouteInfo


url = "https://wiki.engr.illinois.edu/download/attachments/220448101/map_data.json?version=1&modificationDate=1360263791000"
url2 = "https://wiki.engr.illinois.edu/download/attachments/220448182/cmi_hub.json?version=1&modificationDate=1360266230000"


def parseCities(data):
    '''
    This function will parse all the cities' information from provided Json file 
    And add parsed city information into city dictionary
    Also update continent dictionary
    '''
    for city in data["metros"]:
        portCity = CityInfo.CityInfo(city["code"], city["name"], city["country"], 
                                    city["continent"], city["timezone"], city["coordinates"], 
                                    city["population"], city["region"])
        QueryingData.cityDicationary[city["name"]] = portCity   #add city to city dictionary
        QueryingData.codeToName[city["code"]] = city["name"]
        UserQuerying.cityToContinent(city["name"], city["continent"])   #classic cities based on continent 

def parseRoutes(data):
    '''
    This function will parse all the routes' information from provided Json file
    And append parse routes information into route list
    Also update hub city dictionary
    '''
    for route in data["routes"]:
        sourceToDestination = RouteInfo.RouteInfo(route["ports"][0], 
                                           route["ports"][1],
                                           route["distance"])
        
        destinationToSource = RouteInfo.RouteInfo(route["ports"][1],
                                                  route["ports"][0],
                                                  route["distance"])
        QueryingData.routeList.append(sourceToDestination)
        QueryingData.routeList.append(destinationToSource)
        UserQuerying.addHubCity(route["ports"][0])
        UserQuerying.addHubCity(route["ports"][1])
    
    

        
class Parser:
    
    myData = urllib2.urlopen(url)
    csAirData = json.load(myData)
    parseCities(csAirData)
    parseRoutes(csAirData)
    
    # Parse Champaign
    myData2 = urllib2.urlopen(url2)
    champaigne = json.load(myData2)
    parseCities(champaigne)
    parseRoutes(champaigne)
    
    
    
    
    
    
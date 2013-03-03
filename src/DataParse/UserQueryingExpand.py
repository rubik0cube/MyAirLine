'''
Created on Feb 26, 2013

@author: shengchao
'''
from DataParse import QueryingData
from DataParse import UserQuerying
from MyGraphLib import CityInfo
from MyGraphLib import RouteInfo
from DataParse import CostHelper
from DataParse import DijkstraAlgorithm
import copy
import json
import re

pstr = "1.Type 1 to change the city's name.\n2.Type 2 to change the city's code.\n3.Type 3 to changed city's country.\n4.Type 4 to change continent.\n5.Type 5 to change time zone.\n6.Type 6 to change coordinates.\n7.Type 7 to change population.\n8.Type 8 to change region.\n9.Type 9 to exit\n"

def removeCity():
    '''
    This function will remove a city from existing cities,
    and update all the relevant data
    '''
    cityName = raw_input("Please enter the city you want to remove: \n")
    
    if cityName in QueryingData.cityDicationary:    #Check if the input city is valid or not
        
        cityCode = UserQuerying.nameToCode(cityName)
        del QueryingData.continent[cityName]        #Remove the city from the continent  
        del QueryingData.cityDicationary[cityName]  #Remove from the cityDicationary
    
        #Remove relevant routes including the remove city   
        deleteRoute = [route for route in QueryingData.routeList if route.takeOffPortCode == cityCode]
        QueryingData.routeList[:] = [route for route in QueryingData.routeList if route.landPortCode != cityCode and route.takeOffPortCode != cityCode]
        for route in deleteRoute:
            UserQuerying.minusHubCity(route.takeOffPortCode)
            UserQuerying.minusHubCity(route.landPortCode)
                   
    else:                       
        print 'Cannot find ' + cityName             #Invalid input
        
        
def removeRoute():
    '''
    This function will remove a particular route,
    And update all the relevant data
    '''
    sourcePortName = raw_input("Please enter the source port you want to remove: \n")
    destPortName = raw_input("Please enter the destination port you want to remove: \n")
    sourcePortCode = UserQuerying.nameToCode(sourcePortName)
    destPortCode = UserQuerying.nameToCode(destPortName)
    
    for route in QueryingData.routeList:        #Remove source to destination
        if route.takeOffPortCode == sourcePortCode and route.landPortCode == destPortCode:
            QueryingData.routeList.remove(route)
            UserQuerying.minusHubCity(sourcePortCode)
            break
    for route in QueryingData.routeList:        #Remove destination to source
        if route.takeOffPortCode == destPortCode and route.landPortCode == sourcePortCode:
            QueryingData.routeList.remove(route)
            UserQuerying.minusHubCity(destPortCode)
            break
            
            
def addCity():
    '''
    This function will add a new city 
    and all the relevant data about that city into existing cities.
    All the data is from user input
    '''
    cityName = raw_input("Please enter city name: \n")
    cityCode = raw_input("Please enter city code: \n")
    country = raw_input("Please enter country: \n")
    continent = raw_input("Please enter continent: \n")
    timezone = raw_input("Please enter timezone: \n")
    latitude = raw_input("Please enter latitude: \n")       # Type should be: S 30
    longitude = raw_input("Please enter longitude: \n")     # Type should be: W 30
    
    while True:         
        population = raw_input("Please enter population: \n")   #Check if the input is valid
        if int(population) > 0:
            break
        
    region = raw_input("Please enter region: \n")
    
    newCoordinates = UserQuerying.formCoordinate(latitude, longitude)   # Get the right format for the coordinates
    newCityInfo = CityInfo.CityInfo(cityCode, cityName, country, continent, int(timezone), newCoordinates, int(population), int(region))
    QueryingData.cityDicationary[cityName] = newCityInfo    # Add the new class into city Dictionary
    QueryingData.codeToName[cityCode] = cityName             # Add the code and the name into code to name dictionary
    UserQuerying.cityToContinent(cityName, continent)       # Add the city into right continent
    
def addRoute():
    '''
    This function will add a new route between two existing cities
    And update all the relevant data
    '''
    sourcePortName = raw_input("Please enter the source port name: \n")
    destPortName = raw_input("Please enter the destination port name: \n")
    
    while True:
        distance = raw_input("Please enter the distance: \n")   #Check if the input is valid
        if int(distance) > 0:
            break
    
    sourcePortCode = UserQuerying.nameToCode(sourcePortName)
    destPortCode = UserQuerying.nameToCode(destPortName)
    
    newSourceToDestination = RouteInfo.RouteInfo(sourcePortCode, destPortCode, int(distance))
    newDestinationToSource = RouteInfo.RouteInfo(destPortCode, sourcePortCode, int(distance))
    
    QueryingData.routeList.append(newSourceToDestination)       #Append source to destination to route list
    QueryingData.routeList.append(newDestinationToSource)       #Append destination to source to route list
        
    UserQuerying.addHubCity(sourcePortCode)     #update hub city data
    UserQuerying.addHubCity(destPortCode)       #update hub city data
    
def editCity():
    '''
    This function will take user's input about a existing city
    And call relative editing function to edit relative data 
    '''
    cityName = raw_input("Please enter the city you want to edit")
    if cityName in QueryingData.cityDicationary: 
        print pstr
        n = raw_input("Please enter a number: \n")
        if int(n) == 1:
            UserQuerying.changeCityName(cityName)
        if int(n) == 2:
            UserQuerying.changeCityCode(cityName)
        if int(n) == 3:
            UserQuerying.changeCountry(cityName)
        if int(n) == 4:
            UserQuerying.changeContinent(cityName)
        if int(n) == 5:
            UserQuerying.changeTimezone(cityName)
        if int(n) == 6:
            UserQuerying.changeCoordinates(cityName)
        if int(n) == 7:
            UserQuerying.changePopulation(cityName)
        if int(n) == 8:
            UserQuerying.changeRegion(cityName)     
    else:
        print cityName + " does not exist."
        
def saveBackToJson():
    '''
    This function will convert latest city and route information
    into Json type and save it in a file called 'outPutJson.json'
    '''
    Jdata = {}
    metro = []
    routes = []
    # format data
    # format each city
    for cityInfo in QueryingData.cityDicationary.itervalues():
        cnode = {}
        cnode["code"] = cityInfo.code
        cnode["name"] = cityInfo.name
        cnode["country"] = cityInfo.country
        cnode["continent"] = cityInfo.continent
        cnode["timezone"] = cityInfo.timezone
        cnode["coordinates"] = cityInfo.coordinates
        cnode["population"] = cityInfo.population
        cnode["region"] = cityInfo.region
        metro.append(cnode)
    # format each route
    newRouteList = copy.deepcopy(QueryingData.routeList)
    for route in newRouteList:
        sourcePortCode = route.takeOffPortCode
        for item in newRouteList:
            if item.landPortCode == sourcePortCode:
                newRouteList.remove(item)
    for route in newRouteList:
        rnode = {}
        edge = []
        edge.append(route.takeOffPortCode)
        edge.append(route.landPortCode)
        rnode["distance"] = route.distance
        rnode["ports"] = edge
        routes.append(rnode)
        
    Jdata["metros"] = metro
    Jdata["routes"] = routes
    print Jdata
    json.dump(Jdata, open('outPutJson.json', 'w'), indent = 3)
        
def getRouteInfo():
    '''
    This function will call relative functions to calculate 
    distance, cost and consuming time about a particular route
    '''
    cities = raw_input("Please enter cities in route: \n")        # city1, city2, city3 ...
    toGoCityList = re.split(', |,| ,', cities)
    print toGoCityList
    distance = CostHelper.calculateDistance(toGoCityList)
    cost = CostHelper.calculateCost(toGoCityList)
    time = CostHelper.calculateTime(toGoCityList)
    
    print "Total distance is: " + str(distance) + " kilometers"
    print "Total cost is: $" + str(cost) 
    print "Total consuming time is: " + str(time) + " hours"
    
    return cost

def getShortestPath():
    '''
    This function will find the shortest path between two cities
    And calculate the distance, cost and consuming time about the
    Shortest path
    '''
    graph = {}
    pathList = None
    source = raw_input("Please enter the source city: \n")
    destionation = raw_input("Please enter the destination city: \n")
    for city in QueryingData.cityDicationary:
        graph[city] = UserQuerying.getFlyToCity(city)
    pathList = DijkstraAlgorithm.shortestPath(graph, source, destionation)
    print "Ths shortest path: "
    for city in pathList:
        print '>' + city
    print ""
    distance = CostHelper.calculateDistance(pathList)
    cost = CostHelper.calculateCost(pathList)
    time = CostHelper.calculateTime(pathList)
    print "Total distance is: " + str(distance) + " kilometers"
    print "Total cost is: $" + str(cost) 
    print "Total consuming time is: " + str(time) + " hours"
    
        
        
    
    
    
    
    
    

            
        
        
        
        
        
        
        
        
        
    

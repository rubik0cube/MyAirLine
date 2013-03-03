'''
Created on Feb 21, 2013

@author: shengchao
'''
from DataParse import Parser
from DataParse import UserQuerying
from DataParse import UserQueryingExpand

queryString = "1.Type 1 to get all the cities that CSAir flies to.\n2.Type 2 to get special information about a special city.\n3.Type 3 to get statical information about CSAir's route network.\n4.Type 4 to map your route.\n5.Type 5 to Add a new City.\n6.Type 6 to Remove a City.\n7.Type 7 to Add a new Route.\n8.Type 8 to remove a Route.\n9.Type 9 to get Route Information.\n10.Type 10 to edit an Existing City.\n11.Type 11 to Saving the route to the disk.\n12.Type 12 to get shortest path between two country.\n13.Type 13 to exit.\n"

Parser.Parser()

while True:
    print '-----------------------------------------------------------------------'
    print queryString
    
    n = raw_input("Please choose a number: \n")
    if n.strip() == '1':
        cityList = UserQuerying.getCityList()
        print 'Here is all cities that CSAir flies to...'
        for city in cityList:
            print city
        print '\n'
        
    elif n.strip() == '2':
        cityName = raw_input("Please type querying city name: \n")
        if UserQuerying.getQueryCity(cityName) == False:
            print 'Sorry, CSAir does not fly to ' + cityName
        print '\n'
        
    elif n.strip() == '3':
        UserQuerying.getStaticalInfomation()
        print '\n'
        
    elif n.strip() == '4':
        cityCode = raw_input("Please type the city's code: \n")
        if UserQuerying.mapCity(cityCode.upper()) == False:
            print "Sorry, the city's code is invalid\n"
        
    elif n.strip() == '5':
        UserQueryingExpand.addCity()
        
    elif n.strip() == '6':
        UserQueryingExpand.removeCity()
        
    elif n.strip() == '7':
        UserQueryingExpand.addRoute()
        
    elif n.strip() == '8':
        UserQueryingExpand.removeRoute()
        
    elif n.strip() == '9':
        UserQueryingExpand.getRouteInfo()
        
    elif n.strip() == '10':
        UserQueryingExpand.editCity()
        
    elif n.strip() == '11':
        UserQueryingExpand.saveBackToJson()
        
    elif n.strip() == '12':
        UserQueryingExpand.getShortestPath()
        
    elif n.strip() == '13':
        break
    
    else:
        print 'Please give a valid input...'
    
'''
Created on Feb 20, 2013

@author: shengchao
'''
import webbrowser
import QueryingData
import Parser
import pprint

############################################################
def getCityList():
    cityList =[]
    for city in QueryingData.cityDicationary:
        cityList.append(city)
    return cityList
        
def longestFlight():
    currentLongest = 0
    for route in QueryingData.routeList:
        if route.distance > currentLongest:
            currentLongest = route.distance
        
    QueryingData.longestSingleFlight = currentLongest
    return QueryingData.longestSingleFlight

def shortestFlight():
    currentShortest = 10000000
    for route in QueryingData.routeList:
        if route.distance < currentShortest:
            currentShortest = route.distance
            
    QueryingData.shortestSingleFlight = currentShortest
    return QueryingData.shortestSingleFlight

def averageDistance():
    totalDistance = 0
    for route in QueryingData.routeList:
        totalDistance += route.distance
    
    QueryingData.averageDistance = totalDistance/len(QueryingData.routeList)
    return QueryingData.averageDistance
        
def biggestCity():
    currentBiggest = 0
    for cityName, cityInfo in QueryingData.cityDicationary.iteritems():
        if cityInfo.population > currentBiggest :
            currentBiggest = cityInfo.population
            
    QueryingData.biggestCity = currentBiggest
    return QueryingData.biggestCity

def smallestCity():
    currentSmallest = 1000000000
    for cityName, cityInfo in QueryingData.cityDicationary.iteritems():
        if cityInfo.population < currentSmallest:
            currentSmallest = cityInfo.population
        
    QueryingData.smallestCity = currentSmallest
    return QueryingData.smallestCity
    
def averageCitySize():
    totalPopulation = 0
    for cityInfo in QueryingData.cityDicationary.itervalues():
        totalPopulation += cityInfo.population
        
    QueryingData.averageCitySize = totalPopulation/len(QueryingData.cityDicationary)
    return QueryingData.averageCitySize

def getHubCityList():
    currentMax = 0
    hubCityList = []
    for numRoute in QueryingData.hubCity.itervalues():
        if numRoute > currentMax:
            currentMax = numRoute
    
    for cityCode, connections in QueryingData.hubCity.iteritems():
        if connections == currentMax:
            hubCityList.append(codeToName(cityCode))
            
    return hubCityList

def codeToName(cityCode):       #Convert city code into city name
    for code, name in QueryingData.codeToName.iteritems():
        if code == cityCode:
            return name
        
def nameToCode(cityName):       #Convert city name into city code
    for code, name in QueryingData.codeToName.iteritems():
        if name == cityName:
            return code
        
def cityInContinent(continent):
    continentString = ""
    for key, value in QueryingData.continent.iteritems():
        if value == continent:
            continentString = continentString + key + ', '
    return continentString
        
def addHubCity(cityCode):       
    if cityCode in QueryingData.hubCity:
        QueryingData.hubCity[cityCode] += 1
    else:
        QueryingData.hubCity[cityCode] = 0
        
def minusHubCity(cityCode):
    QueryingData.hubCity[cityCode] -= 1
    
def cityToContinent(cityName, continent):       #Add city into right continent
    QueryingData.continent[cityName] = continent

#######################################################################
def changeCityName(oldName):
    newName = raw_input("Please enter the new city name: \n")
    # change city information
    for key, value in QueryingData.cityDicationary.iteritems():
        if key == oldName:
            value.name = newName
            QueryingData.cityDicationary[newName] = QueryingData.cityDicationary.pop(oldName)
            break
    # change code to name
    for code, name in QueryingData.codeToName.iteritems():
        if name == oldName:
            QueryingData.codeToName[code] = newName
            break
    # change name in continent
    for key in QueryingData.continent.iterkeys():
        if key == oldName:
            QueryingData.continent[newName] = QueryingData.continent.pop(oldName)
            
def changeCityCode(cityName):
    newCode = raw_input("Please enter the new city code: \n")
    # change city information
    cityInfo = QueryingData.cityDicationary[cityName]
    oldCode = cityInfo.code
    cityInfo.code = newCode
    # change route list
    for route in QueryingData.routeList:
        if route.takeOffPortCode == oldCode:
            route.takeOffPortCode = newCode
        if route.landPortCode == oldCode:
            route.landPortCode = newCode
    # change hub city dictionary
    for key in QueryingData.hubCity.iterkeys():
        if key == oldCode:
            QueryingData.hubCity[newCode] = QueryingData.hubCity.pop(key)
            break
    # change code to name dictionary
    for key in QueryingData.codeToName.iterkeys():
        if key == oldCode:
            QueryingData.codeToName[newCode] = QueryingData.codeToName.pop(key)
            break
            
def changeCountry(cityName):
    newCountry = raw_input("Please enter the new country name for the city: \n")
    cityInfo = QueryingData.cityDicationary[cityName]
    cityInfo.country = newCountry
    
def changeContinent(cityName):
    newContinent = raw_input("Please enter the new continent for the city: \n")
    cityInfo = QueryingData.cityDicationary[cityName]
    cityInfo.continent = newContinent
    # change the continent dictionary
    for key, value in QueryingData.continent.iteritems():
        if key == cityName:
            QueryingData.continent[key] = newContinent
            break
            
def changeTimezone(cityName):
    newTimezone = raw_input("Please enter the new time zone for the city: \n")
    cityInfo = QueryingData.cityDicationary[cityName]
    cityInfo.timezone = int(newTimezone)
    
def changePopulation(cityName):
    newPopulation = raw_input("Please enter the new population for the city: \n")
    cityInfo = QueryingData.cityDicationary[cityName]
    cityInfo.population = int(newPopulation)
    
def changeRegion(cityName):
    newRegion = raw_input("Please enter the new region for the city: \n")
    cityInfo = QueryingData.cityDicationary[cityName]
    cityInfo.region = int(newRegion)
    
def changeCoordinates(cityName):
    newLatitude = raw_input("Please enter the new latitude: \n")       # S 30
    newLongitude = raw_input("Please enter the new longitude: \n")
    newCoordinates = formCoordinate(newLatitude, newLongitude)
    
    cityInfo = QueryingData.cityDicationary[cityName]
    cityInfo.coordinates = newCoordinates
                                              
##########################################################################       
def getFlyToCity(sourceCity):
    sourceCode = nameToCode(sourceCity)

    destinationList = {}
    for route in QueryingData.routeList:
        if route.takeOffPortCode == sourceCode:
            landCode = route.landPortCode
            landCity = codeToName(landCode)
            destinationList[landCity] = route.distance
            
    return destinationList

def formCoordinate(lati, longti):       #Form coordinate type as like: {S: 30, W: 40}
    coordinate = {}
    latiName = lati.split()[0]
    latiNum = lati.split()[1]
    longtiName = longti.split()[0]
    longtiNum = longti.split()[1]
    coordinate[latiName] = int(latiNum)
    coordinate[longtiName] = int(longtiNum)
    
    return coordinate
        
        
def getQueryCity(cityName):
    for city in QueryingData.cityDicationary:
        if cityName == city:
            queryCity = QueryingData.cityDicationary[city]
            print 'Name: ' + queryCity.name
            print 'Code: ' + queryCity.code
            print 'Country: ' + queryCity.country
            print 'Timezone: ' + str(queryCity.timezone)
            print 'Population: ' + str(queryCity.population)
            print 'Region: ' + str(queryCity.region)
            
            coordinatesList = []
            for n, m in queryCity.coordinates.iteritems():
                corString = n + ': ' + str(m)
                coordinatesList.append(corString)
            print coordinatesList
            
            flyToList = getFlyToCity(cityName)
            print '\nFly To Cities and Distance: '
            for flyToCities, distance in flyToList.iteritems():
                print  flyToCities + ': ' + str(distance) + ' km' 
            return True
    print cityName + " does not exist"
    return False
    
                
def getStaticalInfomation():    
    print 'The Longest Flight: ' + str(longestFlight()) + ' km'
    print 'The ShortesFlight: ' + str(shortestFlight()) + ' km'
    print 'The Average Distance: ' + str(averageDistance()) + ' km'
    print 'The Biggest City Population: ' + str(biggestCity()) 
    print 'The Smallest City Population: ' + str(smallestCity())
    print 'The Average City Population: ' + str(averageCitySize()) + '\n'
    print 'Asia:'
    print cityInContinent("Asia")
    print 'Europe:'
    print cityInContinent("Europe")
    print 'North America:'
    print cityInContinent("North America")
    print 'South America:'
    print cityInContinent("South America")
    print 'Africa:'
    print cityInContinent("Africa") + '\n'
    hubList = getHubCityList()
    print 'Hub Cities: ' 
    for item in hubList:
        print item
        
def mapCity(cityCode):
    url = "http://www.gcmap.com/mapui?P="
    validCode = False
    for item in QueryingData.routeList:
        if item.takeOffPortCode == cityCode:
            url = url + cityCode + '-' + item.landPortCode + ','
            validCode = True
    webbrowser.open_new_tab(url)
    return validCode
    
    
    
    
    
    
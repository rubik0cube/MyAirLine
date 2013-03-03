'''
Created on Feb 28, 2013

@author: shengchao
'''
from DataParse import UserQuerying
from DataParse import QueryingData
import math

def calculateDistance(cityList):
    distance = 0
    counter = len(cityList)
    i = 0
    while counter > 1:
        nextCity = cityList[i+1]
        flyToCityDic = UserQuerying.getFlyToCity(cityList[i])
        distanceToNextCity = flyToCityDic[nextCity]
        distance += distanceToNextCity
        counter -= 1
        i += 1
    return distance
    
def calculateCost(cityList):
    cost = 0
    counter = len(cityList)
    i = 0
    while counter > 1:
        nextCity = cityList[i+1]
        flyToCityDic = UserQuerying.getFlyToCity(cityList[i])
        distanceToNextCity = flyToCityDic[nextCity]
        
        rate = 0.35 - 0.05*i
        if rate <= 0:
            rate = 0
        cost = cost + distanceToNextCity*rate
        
        counter -= 1
        i += 1
    return cost
    
def calculateTime(cityList):
    flyingTime = 0.0
    layoverTime = 0.0
    acceleration = 750.0*750/(2*200)
    counter = len(cityList)
    i = 0
    while counter > 1:
        nextCity = cityList[i+1]
        flyToCityDic = UserQuerying.getFlyToCity(cityList[i])
        distanceToNextCity = flyToCityDic[nextCity]
        # calculate the flying time
        if distanceToNextCity >= 400:
            accTime = 200.0*2/750
            decTime = accTime
            cruisingTime = (distanceToNextCity - 400.0)/750
            flyingTime = flyingTime + accTime + decTime + cruisingTime
        else:
            accTime = math.sqrt(2*distanceToNextCity/acceleration)
            flyingTime = flyingTime + 2*accTime
        # calculate the layover time
        if i != 0:
            cityCode = UserQuerying.nameToCode(cityList[i])
            hubNumber = QueryingData.hubCity[cityCode]
            waitingTime = (120.0 - hubNumber*10)/60 
            layoverTime = layoverTime + waitingTime
        counter -= 1
        i += 1
      
    return (flyingTime + layoverTime)
            
            
    
    
    
    
    
    
    
    
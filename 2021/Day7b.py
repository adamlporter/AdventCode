#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:12:10 2021

@author: alp
"""

testData = [16,1,2,0,4,2,7,1,2,14]

def cleanData(lines):
    for line in lines:
        data = line.split(',')
        data = [int(i) for i in data]
    return data    

def getData():
    with open('Day07Input.txt') as f:  
        lines = f.readlines()
    return cleanData(lines)

def makeLookup(maxVal):
    dd= {}
    stepVal = 0
    for i in range(0,maxVal):
        stepVal += i
        dd[i] = stepVal
    return dd
    
def fuelUsed(points,value,dd):
    total = 0
    for point in points:
        total += dd[abs(point-value)]        
    return total

data = getData()
#data = testData
lookup = makeLookup(max(data))

minFuel = 10**8
minVal = 0

for val in range(460,490):
    fuelBurned = fuelUsed(data,val,lookup)
    if fuelBurned < minFuel:
        minFuel = fuelBurned
        minVal = val
    print(val,fuelBurned)

print(minVal,minFuel)

'''
478 96086265

'''
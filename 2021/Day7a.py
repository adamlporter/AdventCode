#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:12:10 2021

@author: alp
"""

testData = '16,1,2,0,4,2,7,1,2,14'

def cleanData(lines):
    for line in lines:
        data = line.split(',')
        data = [int(i) for i in data]
    return data    

def getData():
    with open('Day07Input.txt') as f:  
        lines = f.readlines()
    return cleanData(lines)
    
def fuelUsed(points,value):
    total = 0
    for point in points:
        total += abs(point - value)
    return total


data = getData()

minFuel = 10**6
minVal = 0

for val in range(0,1923):
    fuelBurned = fuelUsed(data,val)
    if fuelBurned < minFuel:
        minFuel = fuelBurned
        minVal = val





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:53:20 2021

@author: alp
"""

def testbit(bitval,nData):
    if bitval > nData/2:
        return '1'
    else:
        return '0'
    
def testCommonBit(pos,values):
    n0 = n1 = 0
    for val in values:
        if val[pos] == '1':
            n1 += 1
        else:
            n0 += 1
    
    if n0 > n1:
        return '0'
    else:
        return '1'

def cullList(pos,val,origList):
    newList = []
    for item in origList:
        if item[pos] == val:
            newList.append(item)
    
    return newList

with open('Day03Input.txt') as f:
    lines = f.readlines()

data = []

for line in lines:
    data.append(line)


o2 = co2 = data

#['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

position = 0
while len(o2) > 1:
    commonBit = testCommonBit(position,o2)
    o2 = cullList(position,commonBit,o2)
    position += 1
    
print(o2)
print(int(o2[0],2))

position = 0
while len(co2) > 1:
    commonBit = testCommonBit(position,co2)
    if commonBit == '1': 
        commonBit = '0'
    else:
        commonBit = '1'
    co2 = cullList(position,commonBit,co2)
    position += 1
    
print(co2)
print(int(co2[0],2))
print('product = ',int(o2[0],2) * int(co2[0],2))
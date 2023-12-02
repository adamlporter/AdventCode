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

with open('Day03Input.txt') as f:
    lines = f.readlines()

data = []

for line in lines:
    data.append(line)

#data = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

dd = {}

for i in range(len(data[1])-1):
    dd[i] = 0

for item in data:
    for i in range(len(item)-1):
        dd[i] += int(item[i])

gamma = epsilon = ''

for i in range(len(data[1])-1):
    bitval = testbit(dd[i],len(data))
    gamma += bitval
    if bitval == '1' : 
        epsilon += '0'
    else: 
        epsilon += '1'

print('gamma =',int(gamma,2))
print('epsilon =',int(epsilon,2))
print('product =',int(gamma,2) * int(epsilon,2))

    
    

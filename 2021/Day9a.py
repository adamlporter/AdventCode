#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:07:00 2021

@author: alp
"""

def findLowPoints(l0,l1,l2):
    lowPointsValue = 0
    for i in range(1,len(l1)-1):
        if l1[i] < l1[i-1] and l1[i] < l1[i+1] and l1[i] < l0[i] and l1[i] < l2[i]:
            lowPointsValue += int(l1[i]) + 1
    return lowPointsValue

allLowValues = 0 
with open('Day09Input.txt') as f:
    l1 = '9' + f.readline().strip() + '9'
    l0 = '9' * len(l1)
    #allLowPoints = []
    for line in f:
        l2 = '9' + line.strip() + '9'
        #allLowPoints.append(findLowPoints(l0,l1,l2))
        allLowValues += findLowPoints(l0,l1,l2) 
        l0 = l1
        l1 = l2
l2 = '9' * len(l1)
allLowValues += findLowPoints(l0,l1,l2)

print(allLowValues)

# 531 = too low
# 541 correct
             
'''

sample = ['2199943210','3987894921','9856789892','8767896789','9899965678']
#allLowPoints = []
allLowValues = 0
l1 = '9' + sample[0] +'9'
l0 = '9' * len(l1)
for i in range(1,len(sample)):
    l2 = '9' + sample[i] + '9'
    #allLowPoints.append(findLowPoints(l0,l1,l2))
    allLowValues += findLowPoints(l0,l1,l2)
    l0 = l1
    l1 = l2
l2= '9' * len(l1)
#allLowPoints.append(findLowPoints(l0,l1,l2))
allLowValues += findLowPoints(l0,l1,l2)

print(allLowValues)  

'''


        
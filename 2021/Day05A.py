#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 20:21:10 2021

@author: alp
"""


def getData():
    with open('Day05Input.txt') as f:  
        lines = f.readlines()
    return lines
    
def processData(data):
    cleanList = []
    for d in data:
        p1,p2 = d.split(' -> ')
        p1 = p1.split(',')
        p2 = p2.split(',')
        p1 = [int(i) for i in p1]
        p2 = [int(i) for i in p2]
        cleanList.append([p1,p2])
        
    return cleanList

def makeLine(pair):
    line = []
    x1 = pair[0][0]
    y1 = pair[0][1]
    x2 = pair[1][0]
    y2 = pair[1][1]
    
    if x1 == x2:
        if y2 < y1:
            z = y2
            y2 = y1
            y1 = z
        for i in range(y1,y2+1):
            line.append([x1,i])
        print('line from ',x1,y2,' to ',x2,y2)
        
    elif y1 == y2:
        if x2 < x1:
            z = x2
            x2 = x1
            x1 = z
        for i in range(x1,x2+1):
            line.append([i,y1])
        print('line from ',x1,y2,' to ',x2,y2)
    return line
             
pts = processData(getData())

database = []
hits = []

for point in pts:
    newline = makeLine(point)
    for pt in newline:
        if pt in database and pt not in hits:
            hits.append(pt)
        database.append(pt)

print(len(hits))
                
            
    


    
        
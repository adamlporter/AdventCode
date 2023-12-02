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


data = ['0,9 -> 5,9',
        '8,0 -> 0,8',
        '9,4 -> 3,4',
        '2,2 -> 2,1',
        '7,0 -> 7,4',
        '6,4 -> 2,0',
        '0,9 -> 2,9',
        '3,4 -> 1,4',
        '0,0 -> 8,8',
        '5,5 -> 8,2']

    
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

def lineUp(x1,y1,x2,y2):
    line = []
    for i in range (abs(x2-x1)+1):
        line.append([x1+i,y1+i])
    return line

def lineDown(x1,y1,x2,y2):
    line = []
    for i in range (abs(x2-x1)+1):
        line.append([x1+i,y1-i])
    return line

def swapPoints(x1,y1,x2,y2):
    x3 = x2
    x2=x1
    x1=x3
    y3=y2
    y2=y1
    y1=y3
    return x1,y1,x2,y2

def makeDiags(x1,y1,x2,y2):
    if x2 > x1 and y2 > y1 :
        return(lineUp(x1,y1,x2,y2))
    if x2 < x1 and y2 < y1:
        x1,y1,x2,y2 = swapPoints(x1,y1,x2,y2)
        return(lineUp(x1,y1,x2,y2))
    if x2 > x1 and y2 < y1:
        return(lineDown(x1,y1,x2,y2))
    if x2 < x1 and y2 > y1:
        x1,y1,x2,y2 = swapPoints(x1,y1,x2,y2)
        return(lineDown(x1,y1,x2,y2))        

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
#        print('line from ',x1,y1,' to ',x2,y2)
        
    elif y1 == y2:
        if x2 < x1:
            z = x2
            x2 = x1
            x1 = z
        for i in range(x1,x2+1):
            line.append([i,y1])
#        print('line from ',x1,y1,' to ',x2,y2)
    else:
        line = makeDiags(x1,y1,x2,y2)
#        print('diag from ',x1,y1,' to ',x2,y2)

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
                
            
    


    
        
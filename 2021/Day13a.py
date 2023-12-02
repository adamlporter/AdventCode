#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022.02.14

@author: alp
"""

points=[]
folds = []

with open('Day13Input.txt') as f:
    lines = f.readlines()

for line in lines:
    if len(line) < 2:
        pass
    elif len(line) < 10:
        pt = line.split(',')
        pt = [int(i) for i in pt]
        points.append(pt)
    else:
        folds.append(line)

newpoints = []
for fold in folds:
    equalPos = fold.find('=')
    axis = fold[equalPos-1]
    foldVal = int(fold[equalPos+1:])
    # the code above will find the axis along which to fold and the coordinate

    for point in points:
        x,y = point
        if axis == 'x':
            if x > foldVal:
                xNew = foldVal * 2 - x
                newpoints.append([xNew,y])
            else:
                newpoints.append([x,y])
        if axis == 'y':
            if y > foldVal:
                yNew = foldVal * 2 - y
                newpoints.append([x,yNew])
            else:
                newpoints.append([x,y])
#    break
    points = newpoints
    newpoints = []
    # this code will do one set of folds

#points = newpoints
#newpoints = []
for point in points:
    newpoints.append(tuple(point))

print(len(set(newpoints)))

#for the second part, they want to knoe the letters spelled on the paper
import matplotlib.pyplot as plt

plt.scatter(*zip(*newpoints))
# Zip will take the list of tuples and turn it into lists of x values and y values
# then the scatter plot will plot each point
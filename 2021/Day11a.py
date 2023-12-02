#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:07:42 2021

@author: alp
"""

import numpy as np

test = ['5483143223',
        '2745854711',
        '5264556173',
        '6141336146',
        '6357385478',
        '4167524645',
        '2176841721',
        '6882881134',
        '4846848554',
        '5283751526']

def lineToList(line):
    l=[]
    for ch in line:
        l.append(int(ch))
    return l

def getLists(data):
    lists = []
    for line in test:
        lists.append(lineToList(line))
    return lists
    
octos = np.array(getLists(test))
height,width = octos.shape

for step in range(0,10):
    octos += 1
    tens = np.where(octos == 10)
    # find values of 10 in the array
    # iterate over the 10s and increase the adjacent values
    while len(tens[0] > 0):
        for i in range(0,len(tens[0])):
            row = tens[0][i]
            col = tens[1][i]
            for r in range(-1,2):
                for c in range(-1,2):
                    if (row + r >= 0) and (row + r < height
                       ) and (col + c >= 0) and (col + c < width):
                        octos[row + r, col + c] += 1
        tens = np.where(octos == 10)

    
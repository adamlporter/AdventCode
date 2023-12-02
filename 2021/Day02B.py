#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:31:59 2021

@author: alp
"""

#dirs = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']


dirs = []

f=open('Day02Input.txt','r')
lines = f.readlines()

for line in lines:
    dirs.append(line)

h=0
d=0
aim = 0

for dir in dirs:
    goto = dir[0:1]
    dist = int(dir[-2:])
    print(goto,dist)
    if goto == 'u':
        aim -= dist
    elif goto == 'd':
        aim += dist
    else:
        h += dist
        if aim != 0: d += aim * dist
         
print('horiz',h,' depth',d)
print('product is ',h*d)
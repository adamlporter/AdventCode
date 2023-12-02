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

for dir in dirs:
    goto = dir[0:1]
    dist = int(dir[-2:])
    print(goto,dist)
    if goto == 'f':
        h += dist
    elif goto == 'd':
        d += dist
    else:
        d -= dist
        
print('horiz',h,' depth',d)
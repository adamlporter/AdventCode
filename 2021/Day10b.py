#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:01:32 2021

@author: alp
"""

def checkLine(line):
    done = False
    while (not done):
        startLn = len(line)
        line += 'z'
        i = 0
        newline = ''
        while i < len(line):
            if line[i] == ']' or line[i] == ')' or line[i] == '}' or line[i] == '>':
                newline += line[i]
                i += 1
            elif (line[i] == '[' and line[i+1] != ']') or (line[i] == '(' and line[i+1] != ')') or (line[i] == '{' and line[i+1] != '}') or (line[i] == '<' and line[i+1] != '>') :
                newline += line[i]
                i += 1
            else:
                i += 2
        if len(newline) == startLn : 
            done = True
        else:
            line = newline
    
    for i in range(0,len(line)):
        ch = line[i]
        if ch == ')' : 
            return 3
        elif ch == ']':
            return 57
        elif ch == '}':
            return 1197
        elif ch == '>':
            return 25137

def correctLine(line):
    done = False
    while (not done):
        startLn = len(line)
        line += 'z'
        i = 0
        newline = ''
        while i < len(line):
            if line[i] == ']' or line[i] == ')' or line[i] == '}' or line[i] == '>':
                newline += line[i]
                i += 1
            elif (line[i] == '[' and line[i+1] != ']') or (line[i] == '(' and line[i+1] != ')') or (line[i] == '{' and line[i+1] != '}') or (line[i] == '<' and line[i+1] != '>') :
                newline += line[i]
                i += 1
            else:
                i += 2
        if len(newline) == startLn : 
            done = True
            return(newline)
        else:
            line = newline    

def scoreLine(line):
    total = 0
    for ch in line[::-1]:
        total *= 5
        if ch == '(':
            total += 1
        elif ch == '[':
            total += 2
        elif ch == '{':
            total += 3
        elif ch =='<':
            total += 4
    return total
        
             
errors = 0
incompleteLines = []
with open('Day10Input.txt') as f:
    lines = f.readlines()
    for line in lines:
        try:
            errors += checkLine(line)
        except TypeError:
            incompleteLines.append(line)

scores = []
for line in incompleteLines:
    corrections = correctLine(line)
    scores.append(scoreLine(corrections))

# got it right on first try: 3042730309
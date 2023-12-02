#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 21:31:43 2021

@author: alp
"""

test = '{([(<{}[<>[]}>{[]{[(<()>'

def parseLine(line):
    sq = pa = curly = greater = 0
    for ch in line:
        if ch =='[' : 
            sq += 1
        elif ch == '(':
            pa += 1
        elif ch == '{':
            curly += 1
        elif ch == '<':
            greater += 1
        elif ch == ']':
            sq -= 1
        elif ch == ')':
            pa -= 1
        elif ch == '}':
            curly -= 1
        elif ch == '>':
            greater -= 1
    if sq < 0 or pa < 0 or curly < 0 or greater < 0:
        return ch

print(parseLine(test))

notDone = True
line = test
while notDone:
    newline = ''

    i = 0
    while i < len(line):
        if line[i] == ']' or line[i] == ')' or line[i] == '}' or line[i] == '>':
            newline += line[i]
            i += 1
        elif (line[i] == '[' and line[i+1] != ']') or (
                line[i] == '(' and line[i+1] != ')') or (
                line[i] == '{' and line[i+1] != '}') or (
                line[i] == '<' and line[i+1] != '>') :
            newline += line[i]
            i += 2
        
            
                

    
    
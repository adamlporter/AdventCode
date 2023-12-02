# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

with open('Day14Test.txt') as f:
    lines = f.readlines()

dd ={}
for line in lines:
    if len(line) < 2:
        pass
    elif len(line) == 5  :
        poly = line[0:-1]
    else:
        dd[line[0:2]] = line[0] + line[-2:-1] # + line[1]
        #create data dictionary of pairs -> trios with new letter inserted
        
for i in range(0,30):
    newp = ''
    print(i)
    for j in range(0,len(poly)-1):
        pair = poly[j:j+2]
        if pair in dd:
            newp += dd[pair]
        else:
            newp += pair
    newp += poly[-1]
#    print(newp)
    poly = newp

letters = list(set(newp))
for letter in letters:
    print(letter,newp.count(letter))
    
#2619 - wrong
#2634 - wrong
#3435 - Too large
#3406 just right!           
        

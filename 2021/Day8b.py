#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:09:15 2021

@author: alp
"""

test = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
        'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
        'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
        'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
        'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
        'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
        'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
        'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
        'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
        'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']

def getData():  
    with open('Day08Input.txt') as f:  
        lines = [line.strip() for line in f]
    return cleanData(lines)

def cleanData(lines):
    pairs =[]
    for line in lines:
        pair = line.split(' | ')
        pairs.append(pair)
    return pairs

def decodeWord(word,encode):
    wordln = len(word)
    if wordln == 5:
        for i in range(0,wordln):
            letter = word[i]
            if letter == encode['e']:
                return '2'
            elif letter == encode['f']:
                return '3'
            elif letter == encode['b']:
                return '5'
    if wordln == 6:
        return 'X'

data = cleanData(test)
#data = getData()

dd={2:1,3:7,4:4,7:8}

count = 0
for line in data:
    words = line[0].split(' ')
    dd_words = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    encode = {}
    decode ={}
    for word in words:
        for i in range(0,len(word)):
            dd_words[word[i]] += 1
    for key,value in dd_words.items():
        if value == 4:
            decode[key] = 'e'
            encode['e'] = key
        if value == 6:
            decode[key] = 'b'
            encode['b'] = key
        if value == 9:
            decode[key] = 'f'
            encode['f'] = key
        # know new values for b, e, f 
    
    for word in words:
        # len 2 = segments for f & c
        if len(word) == 2:
            for i in range(0,2):
                if word[i] not in decode:
                    decode[word[i]] = 'c'
                    encode['c'] = word[i]
                    break
        # len 3 has f, c, & a
        if len(word) == 3:
            for i in range(0,3):
                if word[i] not in decode:
                    decode[word[i]] = 'a'
                    encode['a'] = word[i]
                    break
        # len 4 has f,c,b, & d
        if len(word) == 4:
            for i in range(0,4):
                if word[i] not in decode:
                    decode[word[i]] = 'd'
                    encode['d'] = word[i]
                    break
        for letter in ['a','b','c','d','e','f','g']:
            if letter not in decode:
                decode[letter] = 'g'
                encode['g'] = letter
     
    numbers = line[1].split(' ')
    for number in numbers:
        valStr = ''
        numlen = len(number)
        if numlen == 2 : 
            valStr += '1'
        elif numlen == 3:
            valStr += '7'
        elif numlen == 4:
            valStr += '4'
        elif numlen == 7:
            valStr += '8'
        else:
            valStr += decodeWord(number,encode)
        print(valStr)
        
        

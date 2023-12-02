#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 22:05:52 2021

@author: alp
"""

import numpy as np

def getData():
    with open('Day04Input.txt') as f:  
        lines = f.readlines()

    balls = lines[0].split(',')
    boards = []
    tempArray=[]
    
    for line in lines[2:]:
        if len(line) > 1:
            tempLine = line.split()
            tempArray.append([int(i) for i in tempLine])
        elif len(line) == 1:
            boards.append(np.array(tempArray))
            tempArray=[]
    return(balls,boards)

def checkBoard(board):
    rows = np.sum(board,axis = 0)
    if -5 in rows:
        return True
    cols = np.sum(board,axis = 1)
    if -5 in cols:
        return True
#    if board[0,0] + board[1,1] + board[2,2] + board[3,3] + board[4,4] == -5:
#        return True
#    if board[0,4] + board[1,3] + board[2,2] + board[3,1] + board[4,0] == -5:
#        return True
    return False

def playBingo(balls,boards):
    for ball in balls:
        boardN = 0
        for board in boards:
            board[board == int(ball)] = -1
            if checkBoard(board):
                print('Bingo! on board',boardN,' when ',ball,' was called.')
                del boards[boardN]
                print(boards)
            boardN += 1

def calcFinal(ball,board):
    board[board == -1] = 0
    boardTotal = 0
    for val in np.sum(board,axis = 0):
        boardTotal += val
    return(boardTotal * ball)

balls,boards = getData()
playBingo(balls,boards)

#print(calcFinal(winBall,winBoard))





                
        
        
        

        

    



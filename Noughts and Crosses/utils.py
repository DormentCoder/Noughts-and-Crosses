import random
import math
from enum import Enum

def evaluate(board): 
    for i in range(0, 3):
        if ( board[i][0] == board[i][1] and board[i][0] == board[i][2]) :
            if (board[i][0] == "X"):
                return  -1
            elif (board[i][0] == "0"):
                return 1
    for i in range(0, 3):
        if ( board[0][i] == board[1][i] and board[0][i] == board[2][i]) :
            if (board[0][i] == "X"):
                return  -1
            elif (board[0][i] == "0"):
                return 1
    if ( board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
        if (board[0][0] == "X"):
            return  -1
        elif (board[0][0] == "0"):
            return 1
    if ( board[2][0] == board[1][1] and board[1][1] == board[0][2]) :
        if (board[1][1] == "X"):
            return  -1
        elif (board[1][1] == "0"):
            return 1    
    return 0

def any_moves_left(board):   
    for i in range(0, 3):
        for j in range(0, 3):
            if not board[i][j]:
                return True
    return False           
  
def has_either_player_won(score):
    return (score != 0)

class Pose():
    x = 0
    y = 0
    def __init__(self, *args): 
        if len(args) > 1:
            self.x = args[0]
            self.y = args[1]
               
    def print(self):
        print('[', self.x, ',', self.y, ']')
        
    def __repr__(self):
        return f"<Pose x:{self.x} y:{self.y}>"
            
    def __str__(self):
        return f"[{self.x},{self.y}]"
        
    def __eq__(self, other):
        if isinstance(other, Pose):
            return (self.x == other.x and self.y == other.y)
        return False
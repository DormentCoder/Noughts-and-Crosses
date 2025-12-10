import world
import random
import config
import utils
import copy

class AIPlayer():
    def __init__(self, world):
        self.world = world

    def make_move(self):  
        return self.minimax( self.world.get_copy_of_board())

    def minimax(self, board):   
        value, move = self.max_value(board)
        return move

    def min_value (self, board):
        utility = utils.evaluate(board) 
        if ( utils.has_either_player_won(utility) or (not utils.any_moves_left(board) ) ) :
            return utility, None
        best_score = 1000
        best_move = None
        for i in range(0,3):
            for j in range(0,3):            
                if (not board[i][j] ) :
                    board[i][j] = "X"
                    move_value, max_move = self.max_value(board)
                    if move_value < best_score :
                        best_score = move_value
                        best_move = utils.Pose(i, j)
                    board[i][j] = ""        
        return best_score, best_move

    def max_value (self, board):
        utility = utils.evaluate(board)
        if ( utils.has_either_player_won(utility) or (not utils.any_moves_left( board) ) ) :
            return utility, None
        best_score = -1000
        best_move = None
        for i in range(0,3):
            for j in range(0,3):
                if (not board[i][j] ) :
                    board[i][j] = "0"
                    move_value, min_move = self.min_value( board )
                    if move_value > best_score:
                        best_score = move_value
                        best_move = utils.Pose(i, j)
                    board[i][j] = ""
        return best_score, best_move
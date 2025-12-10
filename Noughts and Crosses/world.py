import random
import config
import utils
from utils import Pose
from copy import copy, deepcopy

class World():
    def __init__(self):
        self.maxx = config.WORLD_LENGTH - 1
        self.maxy = config.WORLD_BREADTH - 1
        self.location_list = []
        self.cross_locations = []
        self.nought_locations = []
        self.grid = [ ['','',''],
                      ['','',''],
                      ['','','']  ]

    def get_cross_locations(self):
        return self.cross_locations

    def get_nought_locations(self):
        return self.nought_locations
        
    def get_copy_of_board(self):
        return deepcopy(self.grid)
            
    def update_cross_player(self, position):
        self.cross_locations.append(position)
        self.grid[position.x][position.y] = 'X'
        print(self.grid) 
              
    def update_nought_player(self, position):
        self.nought_locations.append(position)
        self.grid[position.x][position.y] = '0'
        print(self.grid)     
       
    def is_finished(self):
        if (utils.evaluate(self.grid) == -1):
            print("Crosses won.")
            return True
        if (utils.evaluate(self.grid) == 1):
            print("Noughts won.")
            return True
        if ((len(self.cross_locations) + len(self.nought_locations)) == 9):
            print("Draw.")
            return True
        return False    
from world import World
from player  import AIPlayer
from environment import Environment
import random
import config
import utils
import time

def play_game():
    world = World()
    player = AIPlayer(world)
    display = Environment(world)
    display.update()  
    while (not world.is_finished()):  
        world.update_cross_player(display.wait_for_mouse_click())        
        display.update() 
        if (not world.is_finished()):
            world.update_nought_player(player.make_move())
            display.update() 
        else:
            break 
    input("Press the Enter key to end game. ")     

if __name__ == "__main__":
    play_game()
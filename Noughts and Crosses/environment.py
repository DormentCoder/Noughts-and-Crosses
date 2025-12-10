from utils import Pose
from graphics import *
import config
import math

class Environment():
    def __init__(self, world, windowName = "World"):
        self.world = world
        self.offset = 10
        self.magnify = 180
        self.cSize = 0.4
        self.oSize = 0.6
        self.pane = GraphWin(windowName, ((2*self.offset)+((self.world.maxx+1)*self.magnify)), ((2*self.offset)+((self.world.maxy+1)*self.magnify)))
        self.pane.setBackground("white")
        self.drawBoundary()
        self.drawGrid()
        self.draw_noughts()
        self.draw_crosses()

    def wait_for_mouse_click(self):
        click_pos = self.pane.getMouse()
        return (self.convert_click(click_pos.x, click_pos.y))

    def drawBoundary(self):
        rect = Rectangle(self.convert(0, 0), self.convert(self.world.maxx+1, self.world.maxy+1))
        rect.draw(self.pane)

    def drawGrid(self):
        vLines = []
        for i in range(self.world.maxx+1):
            vLines.append(Line(self.convert(i, 0), self.convert(i, self.world.maxy+1)))
        for line in vLines:
            line.draw(self.pane)
        hLines = []
        for i in range(self.world.maxy + 1):
            hLines.append(Line(self.convert(0, i), self.convert(self.world.maxx+1, i)))
        for line in hLines:
            line.draw(self.pane)

    def draw_noughts(self):
        self.nought_counters = []
        for i in range(len(self.world.get_nought_locations())):
            self.nought_counters.append( Image(self.convert2(self.world.get_nought_locations()[i].x, self.world.get_nought_locations()[i].y), "images/o.png") ) 
            self.nought_counters[i].draw(self.pane)
            
    def draw_crosses(self):
        self.cross_counters = []
        for i in range(len(self.world.get_cross_locations())):
            self.cross_counters.append( Image(self.convert2(self.world.get_cross_locations()[i].x, self.world.get_cross_locations()[i].y), "images/x.png") ) 
            self.cross_counters[i].draw(self.pane)
    
    def update(self):
        for nought in self.nought_counters: 
            nought.undraw()
        for cross in self.cross_counters: 
            cross.undraw()
            
        self.draw_noughts()
        self.draw_crosses()

    def convert_click(self, x, y):
        newX = math.floor((x - self.offset) / self.magnify) 
        newY = math.floor((y - self.offset)  / self.magnify)
        return Pose(newX, newY)
 
    def convert(self, x, y):
        newX = self.offset + (x * self.magnify)
        newY = self.offset + (y * self.magnify)
        return Point(newX, newY)

    def convert2(self, x ,y):
        newX = (self.offset + 0.5*self.magnify) + (x * self.magnify)
        newY = (self.offset + 0.5*self.magnify) + (y * self.magnify)
        return Point(newX, newY)
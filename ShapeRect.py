from PositionalVectors import Vector2
import pygame

# Rectangle class
class Rect():

    # basic constructor, position, dimensions and color included
    def __init__(self, pos : Vector2, dimensions : Vector2, color : (int,int,int)):
        self.pos = pos
        self.dimensions = dimensions
        self.color = color
        # Creating an object that the pygame renderer has to do no conversions for
        self.pygameRect = pygame.Rect(pos.x,pos.y,dimensions.x,dimensions.y)
    
    # getter function, position, Vector2
    def getPosition(self):
        return self.pos
    
    # getter function, position, Array
    def getPositionArray(self):
        return [self.pos.x, self.pos.y]

    # getter function, dimensions, Vector2
    def getDimensions(self):
        return self.dimensions

    # getter function, dimensions, Array
    def getDimensionsArray(self):
        return [self.dimensions.x, self.dimensions.y]
    
    # getter function, color, tuple
    def getColor(self):
        return self.color

    # getter function for python rect
    def getPygameRect(self):
        return self.pygameRect



    



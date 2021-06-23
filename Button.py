
from ShapeRectBorder import RectBorder
from PositionalVectors import Vector2
import Text
import pygame

class Button(RectBorder):
    
    # constructor
    def __init__(self, pos : Vector2, dimensions : Vector2, color : (int,int,int), borderWidth : int, borderColor : (int,int,int), characters : '', textColor : (int,int,int), textPosition : Vector2):
        self.pos = pos
        self.dimensions = dimensions
        self.color = color
        
        # Creating an object that the pygame renderer has to do no conversions for
        self.pygameRect = pygame.Rect(pos.x,pos.y,dimensions.x,dimensions.y)
        
        # Creating the border of the object and color of the border
        self.borderWidth = borderWidth
        self.borderColor = borderColor

        # Creating the border rectangle that is going nto be behind the first
        self.borderRectangles = pygame.Rect(pos.x - borderWidth, pos.y - borderWidth, dimensions.x + borderWidth * 2, dimensions.y + borderWidth * 2)

        # Information about the text
        self.textInfo = Text.textInformation(textPosition, textColor, characters)

        # Pressing the button information
        self.isPressed = False

    def getTextInformation():
        return self.textInfo

        
        
    
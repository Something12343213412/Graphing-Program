
from ShapeRectBorder import RectBorder
from PositionalVectors import *
import Text
import pygame
import EventHandler
import Shapes
from Mouse import *

class Button(RectBorder):
    
    def WhenExit(self):
        self.color = self.baseColor

    def WhenClicked(self):
        self.color = self.colorWhenClicked

    def WhenHovered(self):
        self.color = self.colorWhenHovered

    def addOnHoveredCall(self, input):
        self.OnHovered.append(input)

    def addOnClickedCall(self, input):
        self.OnClicked.append(input)

    def addOnExitCall(self, input):
        self.OnExit.append(input)


    # constructor
    def __init__(self, pos : Vector2, dimensions : Vector2, color : (int,int,int), borderWidth : int, borderColor : (int,int,int), characters : '', textColor : (int,int,int), textPosition : Vector2, textSize = 20):
        self.pos = pos
        self.dimensions = dimensions
        self.color = color
        self.baseColor = color

        self.OnHovered = []
        self.OnClicked = []
        self.OnExit = []

        

        # adding a color when clicked
        self.colorWhenClicked = (color[0]/2,color[1]/2,color[2]/2)

        # adding a color when pressed
        self.colorWhenHovered = (color[0] + 30, color[1] + 30, color[2] + 30)
        
        # Creating the borders of the collision box
        self.collider = RectangleBorders(pos, dimensions, borderWidth)


        # Creating an object that the pygame renderer has to do no conversions for
        self.pygameRect = pygame.Rect(pos.x,pos.y,dimensions.x,dimensions.y)
        
        # Creating the border of the object and color of the border
        self.borderWidth = borderWidth
        self.borderColor = borderColor

        # Creating the border rectangle that is going nto be behind the first
        self.borderRectangles = pygame.Rect(pos.x - borderWidth, pos.y - borderWidth, dimensions.x + borderWidth * 2, dimensions.y + borderWidth * 2)

        # Information about the text
        self.textInfo = Text.textInformation(textPosition, textColor, characters, textSize)

        # Pressing the button information
        self.isPressed = False
        self.isHovered = False

        # making the position of the text reletive to the button
        self.textInfo.pos.x += pos.x
        self.textInfo.pos.y += pos.y
         
        self.OnExit.append(self.WhenExit)

        self.addOnClickedCall(self.WhenClicked)
        
        self.OnHovered.append(self.WhenHovered) 

        Shapes.buttons.append(self)





    def getTextInformation(self):
        return self.textInfo

    def changeText(self,text):
        self.textInfo.characters = text

    def isPointerOver(self):
        mousePosition = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        # Collision logic
        if(mousePosition.x > self.collider.leftBorder and mousePosition.x < self.collider.rightBorder and mousePosition.y > self.collider.upperBorder and mousePosition.y < self.collider.lowerBorder):
            for i in self.OnHovered:
                i()
            self.isHovered = True

        else:
            if self.isHovered:
                for i in self.OnExit:
                    i()
                    self.isHovered = False

    def isClicked(self):
        self.isPointerOver()
        if(mouse.isReleased and self.isHovered):
            # Budget Solution for now until we add an event system
            self.color = self.colorWhenClicked
            for i in self.OnClicked:
                i()




    
            
        
    
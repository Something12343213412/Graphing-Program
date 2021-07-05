import Button
import pygame
import Text

class InputBox(Button.button):
    
    # Constructor
    def __init__(self, pos : Vector2, dimensions : Vector2, color : (int,int,int), borderWidth : int, borderColor : (int,int,int), characters : '', textColor : (int,int,int), textPosition : Vector2, event : int, textSize = 20):
        self.pos = pos
        self.dimensions = dimensions
        self.color = color
        self.baseColor = color

        # adding the event that the button is linked to
        self.linkedEvent = event

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



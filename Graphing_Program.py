# imports
import pygame
from PositionalVectors import Vector2
from ShapeLine import Line
from ShapeRect import Rect
from ShapeRectBorder import RectBorder
from Button import Button
import Rendering
import Text

# Creating the screen
size = width, height = 400,400
screen = pygame.display.set_mode(size)

# Creating an array to hold all the different lines in the program
lines = []

# Creating a new line

# Example of how to add a line : lines.append(Line(Vector2(1,1), Vector2(200,200),[200,50,50],10))

# Creating an array to hold all the different rectangles in the program
rectangles = []

# creating an array to hold all the different rectangles with borders in the program
borderRectangles = []

# Creating a new rectangle
rectangles.append(Rect(Vector2(0,0),Vector2(400,400),[50,50,200]))

# Creating a new rectangle with a border
#borderRectangles.append(RectBorder(Vector2(100,100),Vector2(20,20),[75,75,150],5,[0,0,0]))

# Creating an array to hold all the buttons
buttons = []

# adding objects to the buttons list
buttons.append(Button(Vector2(100,100),Vector2(60,60),[75,75,150],5,[0,0,0], "test",[255,255,255], Vector2(110,110)))

while True:

    # Drawing Lines
    Rendering.drawLines(lines)

    # Drawing Rectangles
    Rendering.drawRectangles(rectangles)

    # Drawing Rectangles Borders
    Rendering.drawRectanglesBorder(borderRectangles)

    # Drawing Buttons
    Rendering.drawButtons(buttons)

    # Displaying everything
    pygame.display.flip()
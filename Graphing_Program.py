# imports
import pygame
from PositionalVectors import Vector2
from ShapeLine import Line
from ShapeRect import Rect
from ShapeRectBorder import RectBorder
import Rendering

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
borderRectangles.append(RectBorder(Vector2(100,100),Vector2(20,20),[75,75,150],5,[0,0,0]))

while True:
    
    # Drawing Lines
    for i in range(len(lines)):
        pygame.draw.line(Rendering.screen, lines[i].getColor(), lines[i].getStartingPositionArray(), lines[i].getEndingPositionArray(), lines[i].getWidth())

    # Drawing Rectangles
    for i in range(len(rectangles)):
        pygame.draw.rect(Rendering.screen, rectangles[i].getColor(), rectangles[i].getPygameRect())

    # Drawing Rectangles Borders
    for i in range(len(borderRectangles)):
        # Drawing the border first
        pygame.draw.rect(Rendering.screen, borderRectangles[i].getRectBorderColor(), borderRectangles[i].getPygameBorderRectangles())
        # Drawing the actual rectangle
        pygame.draw.rect(Rendering.screen, borderRectangles[i].getColor(), borderRectangles[i].getPygameRect())


    pygame.display.flip()
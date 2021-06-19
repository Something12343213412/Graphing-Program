# imports
import pygame
from PositionalVectors import Vector2
from ShapeLine import Line
from ShapeRect import Rect

size = width, height = 400,400
screen = pygame.display.set_mode(size)

# Creating an array to hold all the different lines in the program
lines = []

# Creating a new line

# Example of how to add a line : lines.append(Line(Vector2(1,1), Vector2(200,200),[200,50,50],10))

# Creating an array to hold all the different rectangles in the program
rectangles = []

# Creating a new rectangle
rectangles.append(Rect(Vector2(0,0),Vector2(400,400),[50,50,200]))

while True:
    

    # Drawing Lines
    for i in range(len(lines)):
        pygame.draw.line(screen, lines[i].getColor(), lines[i].getStartingPositionArray(), lines[i].getEndingPositionArray(), lines[i].getWidth())

    # Drawing Rectangles
    for i in range(len(rectangles)):
        pygame.draw.rect(screen, rectangles[i].getColor(), rectangles[i].getPygameRect())

    pygame.display.flip()
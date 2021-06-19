import pygame
from PositionalVectors import Vector2
from Shape import Line

size = width, height = 400,400
screen = pygame.display.set_mode(size)

# Creating an array to hold all the different lines in the program
lines = []

# Creating a new line
lines.append(Line(Vector2(1,1), Vector2(200,200),[200,50,50],10))

while True:
    


    for i in range(len(lines)):
        pygame.draw.line(screen, lines[i].getColor(), lines[i].getStartingPositionArray(), lines[i].getEndingPositionArray())

    pygame.display.flip()
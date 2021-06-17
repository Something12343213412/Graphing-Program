import pygame
from PositionalVectors import Vector2
from Shape import Line

size = width, height = 400,400
screen = pygame.display.set_mode(size)

# Creating an array to hold all the different lines in the program
lines = []


while True:



    for i in range(len(lines)):
        pygame.draw.line(lines[i])

    pygame.display.flip()
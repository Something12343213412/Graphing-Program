import pygame

# Creating the screen
size = width, height = 400,400
screen = pygame.display.set_mode(size)

def drawLines(lines : []):
    for i in range(len(lines)):
        pygame.draw.line(screen, lines[i].getColor(), lines[i].getStartingPositionArray(), lines[i].getEndingPositionArray(), lines[i].getWidth())
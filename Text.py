import pygame
from PositionalVectors import Vector2

#initilizing font
pygame.font.init()





def displayText(screen, text : '', color : (int,int,int), size, pos : Vector2):
    # attaching the font to a variable
    myfont = pygame.font.SysFont('Comic Sans MS', size)

    # Mapping the font to a variable
    textsurface = myfont.render(text, False, color)

    # displaying screen
    screen.blit(textsurface,(pos.x,pos.y))


class textInformation():
    
    def __init__(position : Vector2, color : (int,int,int), characters : ''):
        self.pos = position
        self.color = color
        self.characters = characters
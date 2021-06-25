import pygame
from PositionalVectors import Vector2

#initilizing font
pygame.font.init()


class textInformation():
    
    def __init__(self, position : Vector2, color : (int,int,int), characters : '', size):
        self.pos = position
        self.color = color
        self.characters = characters
        self.size = size

    def getSize(self):
        return self.size

    def getPosition(self):
        return self.pos

    def getColor(self):
        return self.color

    def getCharacters(self):
        return self.characters


def displayText(screen, text : textInformation):
    # attaching the font to a variable
    myfont = pygame.font.SysFont('Comic Sans MS', text.getSize())
    # Mapping the font to a variable
    textsurface = myfont.render(text.getCharacters(), False, text.getColor())
    # displaying screen
    screen.blit(textsurface,(text.getPosition().x,text.getPosition().y))


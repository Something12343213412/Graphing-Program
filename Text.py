import pygame

#initilizing font
pygame.font.init()


myfont = pygame.font.SysFont('Comic Sans MS', 30)


def displayText(screen, text : '', color : (int,int,int)):
    # Mapping the font to a variable
    textsurface = myfont.render(text, False, color)

    screen.blit(textsurface,(0,0))
import pygame

#initilizing font
pygame.font.init()





def displayText(screen, text : '', color : (int,int,int), size):
    myfont = pygame.font.SysFont('Comic Sans MS', size)

    # Mapping the font to a variable
    textsurface = myfont.render(text, False, color)

    screen.blit(textsurface,(0,0))
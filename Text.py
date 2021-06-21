import pygame

#initilizing font
pygame.font.init()


myfont = pygame.font.SysFont('Comic Sans MS', 30)

# Mapping the font to a variable
textsurface = myfont.render('Some Text', False, (0, 0, 0))
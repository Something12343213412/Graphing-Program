from PositionalVectors import Vector2
import Rendering
import pygame


class Mouse():

    def __init__(self):
        # Getting the mouse position
        self.position = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        # Variable to check if the mouse is currently being clicked
        self.isPressed = False

        # checks if the mouse was released this frame
        self.isReleased = False
    
    def refresh(self):

        # Reseting is released
        self.isReleased = False

        # checking if mouse is released this frame
        if self.isPressed and pygame.mouse.get_pressed()[0] == False:
            self.isReleased = True

        # Reseting is pressed variable
        self.isPressed = pygame.mouse.get_pressed()[0]

        # updating the mouse
        self.position = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


mouse = Mouse()

        





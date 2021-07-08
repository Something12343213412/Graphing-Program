from PositionalVectors import Vector2
import pygame

class mouse():

    def __init(self):
        # Getting the mouse position
        position = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        # Variable to check if the mouse is currently being clicked
        isPressed = False

        # checks if the mouse was released this frame
        isReleased = False
    
    def refresh():

        # Reseting is released
        isReleased = False

        # checking if mouse is released this frame
        if isPressed and pygame.mouse.get_pressed()[0] == False:
            isReleased = True

        # Reseting is pressed variable
        isPressed = pygame.mouse.get_pressed()[0]

        # updating the mouse
        position = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


        





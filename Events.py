import pygame
import Shapes


def testEvent():
    print("test")

def closeProgram():
    pygame.quit()

def startingEvent():
    buttons.append(Button(Vector2(40,40),Vector2(200,60),[75,75,150],5,[0,0,0], "Close Program",[0,255,0], Vector2(40,45),1, 30))
    
def LinkToEvent(event : int):
    if event == 0:
        testEvent()

    if event == 1:
        closeProgram()
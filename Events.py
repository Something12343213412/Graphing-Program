import pygame
import Shapes
import Button
import ShapeRect
from PositionalVectors import Vector2


def testEvent():
    print("test")

def closeProgram():
    pygame.quit()


def startingEvent():
    # Background
    Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (71, 121, 201)))

    # Close Program Button
    Shapes.buttons.append(Button.Button(Vector2(40,40),Vector2(200,60),[75,75,150],5,[0,0,0], "Close Program",[0,255,0], Vector2(0,5),1, 30))

    # Setting Button
    Shapes.buttons.append(Button.Button(Vector2(1000,40),Vector2(150,60),[75,75,150],5,[0,0,0], "Settings",[0,255,0], Vector2(15,5),1, 30))

    
    
    
def linkToEvent(event : int):
    if event == 0:
        testEvent()

    if event == 1:
        closeProgram()

    if event == 2:
        startingEvent()
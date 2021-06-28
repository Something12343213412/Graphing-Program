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
    Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (71, 121, 201)))
    Shapes.buttons.append(Button.Button(Vector2(40,40),Vector2(200,60),[75,75,150],5,[0,0,0], "Close Program",[0,255,0], Vector2(40,45),1, 30))
    
    
def linkToEvent(event : int):
    if event == 0:
        testEvent()

    if event == 1:
        closeProgram()

    if event == 2:
        startingEvent()
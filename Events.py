import pygame
import Shapes
import Button
import Text
import ShapeRect
from PositionalVectors import Vector2


def testEvent():
    print("test")

def closeProgram():
    pygame.quit()

def rollCredits():
    

# Creates the basic home screen, called at the start of the program
def startingEvent():


    # Background
    Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (71, 121, 201)))

    # Close Program Button
    Shapes.buttons.append(Button.Button(Vector2(40,40),Vector2(200,60),[175,75,75],5,[0,0,0], "Close Program",[0,0,0], Vector2(5,5),1, 30))

    # Setting Button
    Shapes.buttons.append(Button.Button(Vector2(1000,40),Vector2(150,60),[75,75,75],5,[0,0,0], "Settings",[0,0,0], Vector2(15,5),1, 30))

    # Start Button
    Shapes.buttons.append(Button.Button(Vector2(390,330),Vector2(500,120),[28, 165, 179],5,[0,0,0], "Start Program",[0,0,0], Vector2(5,5),1, 70))

    # Credits Button
    Shapes.buttons.append(Button.Button(Vector2(580,530),Vector2(120,60),[125,125,125],5,[0,0,0], "Credits",[0,0,0], Vector2(5,5),1, 30))
    
    
    
def linkToEvent(event : int):
    if event == 0:
        testEvent()

    if event == 1:
        closeProgram()

    if event == 2:
        startingEvent()
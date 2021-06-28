import pygame
import Shapes
import Button
import Text
import ShapeRect
from PositionalVectors import Vector2

# Creates the basic home screen, called at the start of the program
def startingEvent():
    Shapes.clearAll()

    # Background
    Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (71, 121, 201)))

    # Close Program Button
    Shapes.buttons.append(Button.Button(Vector2(40,40),Vector2(200,60),[175,75,75],5,[0,0,0], "Close Program",[0,0,0], Vector2(5,5),1, 30))

    # Setting Button
    Shapes.buttons.append(Button.Button(Vector2(1000,40),Vector2(150,60),[75,75,75],5,[0,0,0], "Settings",[0,0,0], Vector2(15,5),5, 30))

    # Start Button
    Shapes.buttons.append(Button.Button(Vector2(390,330),Vector2(500,120),[28, 165, 179],5,[0,0,0], "Start Program",[0,0,0], Vector2(5,5),1, 70))

    # Credits Button
    Shapes.buttons.append(Button.Button(Vector2(580,530),Vector2(120,60),[125,125,125],5,[0,0,0], "Credits",[0,0,0], Vector2(5,5),3, 30))

def testEvent():
    print("test")

def closeProgram():
    pygame.quit()

def settingsMenu():
    Shapes.runLoop = False

    Shapes.clearAll()
    # Background
    Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (75, 75, 75)))

    # Close Program Button
    Shapes.buttons.append(Button.Button(Vector2(40,40),Vector2(200,60),[150,75,75],5,[0,0,0], "Close Program",[0,0,0], Vector2(5,5),1, 30))

    # Back Button
    Shapes.buttons.append(Button.Button(Vector2(40,600),Vector2(75,60),[150,150,150],5,[0,0,0], "Back",[0,0,0], Vector2(5,5),4, 30))

    

def rollCredits():
    Shapes.clearAll()
    # Background
    Shapes.rectangles.append(ShapeRect.Rect(Vector2(0,0), Vector2(1280,720), (0, 0, 0)))

    # Close Program Button
    Shapes.buttons.append(Button.Button(Vector2(40,40),Vector2(200,60),[150,75,75],5,[0,0,0], "Close Program",[0,0,0], Vector2(5,5),1, 30))

    # Back Button
    Shapes.buttons.append(Button.Button(Vector2(40,600),Vector2(75,60),[150,150,150],5,[0,0,0], "Back",[0,0,0], Vector2(5,5),4, 30))

    # Setting Button
    Shapes.buttons.append(Button.Button(Vector2(1000,40),Vector2(150,60),[75,75,75],5,[0,0,0], "Settings",[0,0,0], Vector2(15,5),1, 30))

    # Adding the credits
    Shapes.text.append(Text.textInformation(Vector2(300,300),(175,175,175),"Credits : Kevin Sandberg, Main Programmer",30))
    Shapes.text.append(Text.textInformation(Vector2(300,340),(175,175,175),"Credits : RobertTeaches, Debugger",30))
    
def returnToHome():
    startingEvent()
    
def linkToEvent(event : int):
    if event == 0:
        testEvent()

    if event == 1:
        closeProgram()

    if event == 2:
        startingEvent()

    if event == 3:
        rollCredits()

    if event == 4:
        returnToHome()

    if event == 5:
        settingsMenu()
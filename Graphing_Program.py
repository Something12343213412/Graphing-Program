# imports
import pygame
from PositionalVectors import Vector2
from ShapeLine import Line
from ShapeRect import Rect
from ShapeRectBorder import RectBorder
from Button import Button
import Rendering
import Text
import Shapes
import EventHandler as Events
import State
import Mouse
import Function

# Creating the clock
clock = pygame.time.Clock()

# Calling the starting event
State.state.mainMenu()


Function.test.lineDots(1)

#Shapes.linesOnGraph.append(Function.test.returnLine(0))


while True:

    Mouse.mouse.refresh()

    # Getting the mouse position
    mousePosition = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    # THIS IS A VERY NESCARY LINE OF CODE, NEVER REMOVE IT
    pygame.event.get()

    # Setting the framerate
    clock.tick(60)

    # Drawing Lines
    Rendering.drawLines(Shapes.lines)

    # Drawing Rectangles
    Rendering.drawRectangles(Shapes.rectangles)

    # Drawing Rectangles Borders
    Rendering.drawRectanglesBorder(Shapes.borderRectangles)

    # checking if the cursor is over buttons
    for i in range(len(Shapes.buttons)):
        if Shapes.runLoop:
            Shapes.buttons[i].isClicked()

    Shapes.runLoop = True

    # Drawing Buttons
    Rendering.drawButtons(Shapes.buttons)

    # Drawing Text
    Rendering.DrawText(Shapes.text)

    # Drawing Points
    #Rendering.drawPointsOnPlane(Shapes.linesOnGraph)

    # Drawing Lines on Canvas
    if State.state.currentState == State.graphingMenu:
        Rendering.drawLinesOnPlane(Shapes.linesOnGraph)
        Rendering.drawRectanglesOnPlane(Shapes.RectanglesOnPlane)
        

    # Displaying everything
    pygame.display.flip()
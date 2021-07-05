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

# Creating the clock
clock = pygame.time.Clock()

# Calling the starting event
Events.mainMenu()

while True:

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

    # Displaying everything
    pygame.display.flip()
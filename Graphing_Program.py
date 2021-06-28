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

# Creating the clock
clock = pygame.time.Clock()


# Creating an array to hold all the different lines in the program
lines = []

# Creating a new line

# Example of how to add a line : lines.append(Line(Vector2(1,1), Vector2(200,200),[200,50,50],10))

# Creating an array to hold all the different rectangles in the program
rectangles = []

# creating an array to hold all the different rectangles with borders in the program
borderRectangles = []

# Creating a new rectangle
rectangles.append(Rect(Vector2(0,0),Vector2(400,400),[50,50,200]))

# Creating a new rectangle with a border
#borderRectangles.append(RectBorder(Vector2(100,100),Vector2(20,20),[75,75,150],5,[0,0,0]))

# Creating an array to hold all the buttons
buttons = []

# adding objects to the buttons list
buttons.append(Button(Vector2(40,40),Vector2(200,60),[75,75,150],5,[0,0,0], "Close Program",[0,255,0], Vector2(40,45),1, 30))

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
        Shapes.buttons[i].isClicked()

    # Drawing Buttons
    Rendering.drawButtons(Shapes.buttons)

    # Displaying everything
    pygame.display.flip()
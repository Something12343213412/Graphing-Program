import pygame
import Text

# Creating the screen
size = width, height = 1280,720
screen = pygame.display.set_mode(size)

# Drawing lines
def drawLines(lines : []):
    for i in range(len(lines)):
        pygame.draw.line(screen, lines[i].getColor(), lines[i].getStartingPositionArray(), lines[i].getEndingPositionArray(), lines[i].getWidth())

# Drawing Rectangles
def drawRectangles(rectangles : []):
    for i in range(len(rectangles)):
        pygame.draw.rect(screen, rectangles[i].getColor(), rectangles[i].getPygameRect())

# Drawing Rectangle Borders
def drawRectanglesBorder(borderRectangles : []):
    for i in range(len(borderRectangles)):
        # Drawing the border first
        pygame.draw.rect(screen, borderRectangles[i].getRectBorderColor(), borderRectangles[i].getPygameBorderRectangles())
        # Drawing the actual rectangle
        pygame.draw.rect(screen, borderRectangles[i].getColor(), borderRectangles[i].getPygameRect())

# drawing points on the plane
def drawPointsOnPlane(PointsOnPlane : []):
    for i in range(len(PointsOnPlane)):
        # drawing the point
        pygame.draw.rect(screen, [0,0,0], PointsOnPlane[i].getPygameRect())
        
# draw lines on planes
def drawLinesOnPlane(LinesOnPlane : []):
    for i in range(len(LinesOnPlane)):
        
        LinesOnPlane[i].One.x += 290
        LinesOnPlane[i].Two.x += 290

        LinesOnPlane[i].One.y += 240
        LinesOnPlane[i].Two.y += 240

        #print(LinesOnPlane.one.x + " " + LinesOnPlane.one.y + " " )

    drawLines(LinesOnPlane)

    for i in range(len(LinesOnPlane)):
        
        LinesOnPlane[i].One.x -= 290
        LinesOnPlane[i].Two.x -= 290

        LinesOnPlane[i].One.y -= 240
        LinesOnPlane[i].Two.y -= 240


# Drawing Buttons
def drawButtons(buttons : []):
    drawRectanglesBorder(buttons)

    #Creating a for loop to loop through all the text
    for i in range(len(buttons)):
        Text.displayText(screen, buttons[i].getTextInformation())

# Render Text
def DrawText(text : []):
    for i in range(len(text)):
        Text.displayText(screen, text[i])

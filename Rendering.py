import pygame

# Creating the screen
size = width, height = 400,400
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


# Drawing Buttons
def drawButtons(buttons : []):
    drawRectanglesBorder(buttons)
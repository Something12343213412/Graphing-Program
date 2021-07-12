import ShapeLine
import Shapes
import ShapeRect
from PositionalVectors import Vector2

# Change this file to whatever you path is
f = open("InformationForGraphing.txt", "r")


class function():

    def __init__(self,typeOfLine, b,m):
        self.b = b
        self.m = m
        self.startingPosition = Vector2(0,0)
        self.endingPosition = Vector2(0, 0)
        self.typeOfLine = typeOfLine

    def lineDots(self, viewPortScale, viewPortDimension = Vector2(800,400)):
        if self.typeOfLine == 1:
            self.startingPosition.x = self.b + 290
            self.startingPosition.y = viewPortDimension.y + 240
            #Shapes.RectanglesOnPlane.append(ShapeRect.Rect(Vector2(self.startingPosition.x, self.startingPosition.y), Vector2(2,2),(255,255,255)))

            while self.startingPosition.x <= viewPortDimension.x + 290 and self.startingPosition.y >= viewPortDimension.y - 160 and self.startingPosition.x >= 290 and self.startingPosition.y <= viewPortDimension.y + 240:
                self.startingPosition.x += 1 * self.m
                self.startingPosition.y -= 1
                Shapes.RectanglesOnPlane.append(ShapeRect.Rect(Vector2(self.startingPosition.x, self.startingPosition.y), Vector2(2,2),(255,255,255)))
        
        #if self.typeOfLine == 2:
            #while self.x < 800:
                #self.startingPosition.y = self.startPosition.x^2 + self.startingPosition.x
                #self.startingPosition.x = self.startingPosition.y - self.startingPosition.x^2
            


    def returnLine(self, viewPortScale, viewPortDimension = Vector2(800,400)):

        self.startingPosition = Vector2(self.b, viewPortDimension.y)
        self.endingPosition = Vector2(viewPortDimension.x + self.b, 0)

        if self.endingPosition.x > 800:
            self.endingPosition.y += (self.endingPosition.x - 800)
            self.endingPosition.x = 800

        if self.endingPosition.y > 400:
            self.endingPosition.x += (self.endingPosition.y - 400)
            self.endingPosition.y = 400

        if self.startingPosition.x < 0:
            self.startingPosition.y += (self.startingPosition.x)
            self.startingPosition.x = 0

        if self.startingPosition.y < 0:
            self.startingPosition.x += (self.startingPosition.y)
            self.startingPosition.y = 0

        return ShapeLine.Line(self.startingPosition, self.endingPosition, (255,255,255), 5)

test = function(int(f.readline), int(f.readline()), float(f.readline()))
test.lineDots(1)

test2 = function(int(f.readline), int(f.readline()), float(f.readline()))
test2.lineDots(1)



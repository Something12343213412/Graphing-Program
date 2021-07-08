import ShapeLine
from PositionalVectors import Vector2

# Change this file to whatever you path is
f = open("InformationForGraphing.txt", "r")


class function():

    def __init__(self,b):
        self.b = b
        self.startingPosition = Vector2(0,0)
        self.endingPosition = Vector2(0, 0)

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

test = function(int(f.readline()))



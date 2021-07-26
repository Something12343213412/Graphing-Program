import ShapeLine
import Shapes
import ShapeRect
import math
from PositionalVectors import Vector2

# Change this file to whatever you path is
f = open("InformationForGraphing.txt", "r")

class function():

    def __init__(self,typeOfLine, A : float, B : float, C = 0.0):
        self.A = A
        self.B = B
        self.C = C
        self.startingPosition = Vector2(0,0)
        self.endingPosition = Vector2(0,0)
        self.typeOfLine = typeOfLine
    
    # def furthestLeftMostX(self, viewPortDimension = Vector2(800,400)):
        
    #    while (math.pow(self.startingPosition.x,2)) + self.startingPosition.x < viewPortDimension.y and self.startingPosition.x >= -400:

    #        self.startingPosition.y = (math.pow(self.startingPosition.x,2)) + self.startingPosition.x
    #        self.startingPosition.x -= 0.5

    #    print(self.startingPosition.x + 400)
    #    print(self.startingPosition.y)
    #

    def quadraticFormula(self, a : float ,b : float,c : float):
        print(b)
        return ((-b + math.sqrt(math.pow(b,2) - 4*a*c))/2*a, (-b - math.sqrt(math.pow(b,2) - 4*a*c))/2*a)

    def findVertex(self, a : float, b : float, c : float):
        x = -b/(2*a)
        print('b = ', b)
        print("a = ", a)
        print('x = ', x)

        # to convert this to the quadraticFormula would I just use the quadraticFormula and use the inputs, but then I would need to find y

        return Vector2(x, (a * math.pow(x,2)) + (x * b) + (c))

   
    def plotQuadratic(self, a : float, b : float, c : float, viewPortDimension = Vector2(800,400), viewPortScale = 10.0):
        
        # finding the vertex
        vertex = self.findVertex(a,b,c)
        
        # setting the variables that are going to be used for drawing to be based off the vertex
        y = vertex.y
        x1 = vertex.x
        x2 = vertex.x

        # Corners of the screen in the graph
        leftBottomViewPortOnGraph = Vector2((vertex.x - 4 * viewPortScale), (vertex.y + 6 * viewPortScale))
        topRightViewPortOnGraph = Vector2((vertex.x + 4 * viewPortScale), (vertex.y - 6 * viewPortScale))

        # Corners of the viewport
        leftBottomViewPort = Vector2(290, 640)
        topRightViewPort = Vector2(1090, 240)

        # Aspect Ratio
        aspectRatio = viewPortDimension.x/viewPortDimension.y

        # dotScale
        dotThickness = Vector2(3,3)

        # Color Black
        black = (255,255,255)

        # drawing the vertex
        
        # Gets the distance in the graph units from the point to the bottom left of the graph
        distanceFromBottomLeftGraph = Vector2(abs(x1 - leftBottomViewPortOnGraph.x), abs(y - leftBottomViewPortOnGraph.y))

        # Uses the distance from bottom left then multiplies it by viewport scale and applies the aspect ratio to the y
        distanceFromBottomLeftOfTheViewport = Vector2(distanceFromBottomLeftGraph.x * viewPortScale, (distanceFromBottomLeftGraph.y * viewPortScale) / aspectRatio)

        # Get's the position on the screen based of the viewPort
        positionOnScreen = Vector2(topRightViewPort.x - distanceFromBottomLeftOfTheViewport.x, topRightViewPort.y + distanceFromBottomLeftOfTheViewport.y)

        print("Vertex = ", positionOnScreen.x, ' ', positionOnScreen.y)
        print("Vertex x1 = ", x1, 'Vertex x2', x2, 'Vertex y = ', y)
        print()

        # adds it to an array to draw
        Shapes.RectanglesOnPlane.append(ShapeRect.Rect(positionOnScreen, dotThickness, black))





        # main while loop to draw the function
        while y > topRightViewPortOnGraph.y and y < leftBottomViewPortOnGraph.y:

            x1, x2 =  self.quadraticFormula(float(a), float(b), float(c) - y)

            #print(x1, ' ', x2)

            

            # checking if the positive x is going over the right boundry
            if x1 > leftBottomViewPortOnGraph.x:

                # Gets the distance in the graph units from the point to the bottom lecft of the graph
                distanceFromBottomLeftGraph = Vector2(abs(leftBottomViewPortOnGraph.x - x1), abs(y - leftBottomViewPortOnGraph.y))
               
                # Uses the distance from bottom left then multiplies it by viewport scale and applies the aspect ratio to the y
                distanceFromBottomLeftOfTheViewport = Vector2(distanceFromBottomLeftGraph.x * viewPortScale, (distanceFromBottomLeftGraph.y * viewPortScale) / aspectRatio)

                # Get's the position on the screen based of the viewPort
                positionOnScreen = Vector2(topRightViewPort.x - distanceFromBottomLeftOfTheViewport.x, topRightViewPort.y + distanceFromBottomLeftOfTheViewport.y)
                
                print('1 Position on screen = ', positionOnScreen.x, 'x1 = ', x1)
                print('1 Position on screen = ', positionOnScreen.y, 'y = ', y)
                print("")

                # adds it to an array to draw
                Shapes.RectanglesOnPlane.append(ShapeRect.Rect(positionOnScreen, dotThickness, black))

            # checking if the negetive x is going over the left boundry
            if x2 < topRightViewPortOnGraph.x:

                # Gets the distance in the graph units from the point to the bottom left of the graph
                distanceFromBottomLeftGraph = Vector2(abs(leftBottomViewPortOnGraph.x - x2), abs(y - leftBottomViewPortOnGraph.y))

                # Uses the distance from bottom left then multiplies it by viewport scale and applies the aspect ratio to the y
                distanceFromBottomLeftOfTheViewport = Vector2(distanceFromBottomLeftGraph.x * viewPortScale, (distanceFromBottomLeftGraph.y * viewPortScale) / aspectRatio)

                # Get's the position on the screen based of the viewPort
                positionOnScreen = Vector2(topRightViewPort.x - distanceFromBottomLeftOfTheViewport.x, topRightViewPort.y + distanceFromBottomLeftOfTheViewport.y)

                print('2 Position on screen = ', positionOnScreen.x, 'x2 = ', x2)
                print('2 Position on screen = ', positionOnScreen.y, 'y = ', y)
                print("")

                # adds it to an array to draw
                Shapes.RectanglesOnPlane.append(ShapeRect.Rect(positionOnScreen, dotThickness, black))


            # adding some to y, the 1000 is a number that was pulled out of thin air
            y = y + viewPortScale/1000
        

    def lineDots(self, viewPortScale, viewPortDimension = Vector2(800,400)):
        if self.typeOfLine == 1:
            self.startingPosition.x = self.B + 290
            self.startingPosition.y = viewPortDimension.y + 240
            #Shapes.RectanglesOnPlane.append(ShapeRect.Rect(Vector2(self.startingPosition.x, self.startingPosition.y), Vector2(2,2),(255,255,255)))

            while self.startingPosition.x <= viewPortDimension.x + 290 and self.startingPosition.y >= viewPortDimension.y - 160 and self.startingPosition.x >= 290 and self.startingPosition.y <= viewPortDimension.y + 240:
                self.startingPosition.x += 1 * self.A
                self.startingPosition.y -= 1
                Shapes.RectanglesOnPlane.append(ShapeRect.Rect(Vector2(self.startingPosition.x, self.startingPosition.y), Vector2(2,2),(255,255,255)))
        
        if self.typeOfLine == 2:
            self.plotQuadratic(self.A,self.B,self.C)
            
            

            


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

#test = function(int(f.readline()), int(f.readline()), float(f.readline()))
#test.lineDots(1)

#test2 = function(int(f.readline()), int(f.readline()), float(f.readline()))
#test2.lineDots(1)

test3 = function(int(2), 1, 1,0)
test3.lineDots(1)
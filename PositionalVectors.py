
class Vector2:
    def __init__(self, x : float,y : float):
        self.x = x
        self.y = y

    def add(self, input : 'Vector2'):
        self.x += input.x
        self.y += input.y

    def subtract(self, input : 'Vector2'):
        self.x -= input.x
        self.y -= input.y

    def multiply(self, input : int):
        self.x *= input
        self.y *= input

    def divide(self, input : int):
        self.x /= input
        self.y /= input


class RectangleBorders:

    # init function
    def __init__(self, position : Vector2, dimensions : Vector2, borderSize):
        self.leftBorder = position.x - borderSize/2
        self.upperBorder = position.y - borderSize/2
        self.lowerBorder = position.y + dimensions.y + borderSize/2
        self.rightBorder = position.x + dimensions.x + borderSize/2


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


class Vector2:
    def __init__(x : float,y : float):
        self.x = x
        self.y = y

    def add(input : 'Vector2'):
        self.x += input.x
        self.y += input.y

    def subtract(input : 'Vector2'):
        self.x -= input.x
        self.y -= input.y

    def multiply(input : int):
        self.x *= input
        self.y *= input

    def divide(input : int):
        self.x /= input
        self.y /= input

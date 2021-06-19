from PositionalVectors import Vector2
import pygame

class Line:
    
    def __init__(self, One : Vector2, Two : Vector2, Color : (int,int,int), Width : int):
       self.One = One
       self.Two = Two
       self.Color = Color
       self.Width = Width

    def getStartingPosition(self):
        return self.One
    
    def getEndingPosition(self):
        return self.Two

    def getColor(self):
        return self.Color

    def getWidth(self):
        return self.Width

    def getStartingPositionArray(self):
        return [self.One.x, self.One.y]

    def getEndingPositionArray(self):
        return [self.Two.x, self.Two.y]

from PositionalVectors import Vector2
import pygame

class Line:
    
    def __init__(One : Vector2, Two : Vector2, Color : (int,int,int), Width : int):
       self.One = One
       self.Two = Two
       self.Color = Color
       self.Width = Width

    def getStartingPosition():
        return self.One
    
    def getEndingPosition():
        return self.Two

    def getColor():
        return self.Color

    def getWidth():
        return self.Width


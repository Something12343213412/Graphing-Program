from ShapeRect import Rect


class RectBorder(Rect):
     
    def __init__(self, pos : Vector2, dimensions : Vector2, color : (int,int,int), borderWidth : int, borderColor : (int,int,int)):
        self.pos = pos
        self.dimensions = dimensions
        self.color = color
        
        # Creating an object that the pygame renderer has to do no conversions for
        self.pygameRect = pygame.Rect(pos.x,pos.y,dimensions.x,dimensions.y)
        
        # Creating the border of the object and color of the border
        self.borderWidth = borderWidth
        self.borderColor = borderColor
     



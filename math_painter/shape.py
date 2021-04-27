class Shape:
    colors = {}
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Square(Shape):
    def __init__(self, x, y, side, color, canvas):
        super().__init__(x, y, color)
        self.side = side
        self.canvas = canvas

    def draw(self, canvas):
        return canvas[self.x:(self.x + self.side), self.y:(self.y + self.side)] = 
# data[100:150, 100:200] = [255, 200, 233]

class Rectangle(Shape):
    def __init__(self, x, y, height, width, color, canvas):
        super().__init__(x, y, color)
        self.height = height
        self.width = width
        self.canvas = canvas

    def draw(self, canvas):
        pass

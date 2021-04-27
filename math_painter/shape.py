from color_dict import *
from random import choice

class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        if self.color in colors_dict.keys():
            self.color = color
        else:
            rand_color = choice(list(colors_dict.keys()))
            print(f"Color not recognized. I'm gonna paint it {rand_color}")
            self.color = rand_color

class Rectangle(Shape):
    def __init__(self, x, y, height, width, color, canvas):
        super().__init__(x, y, color)
        self.height = height
        self.width = width
        self.canvas = canvas

    def draw(self, canvas):
        canvas.add_shape(x_start = self.x,
                         x_end = self.x + self.width,
                         y_start = self.y,
                         y_end = self.y + self.height,
                         color = [*get_color(self.color)])
        return canvas

class Square(Rectangle):
    def __init__(self, x, y, side, color, canvas):
        super().__init__(x, y, side, side, color, canvas)
        self.side = side
        self.canvas = canvas

    def draw(self, canvas):
        canvas.add_shape(x_start = self.x,
                         x_end = self.x + self.side,
                         y_start = self.y,
                         y_end = self.y + self.side,
                         color = [*get_color(self.color)])
        return canvas

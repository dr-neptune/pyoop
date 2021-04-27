import numpy as np
from color_dict import *
from PIL import Image

class Canvas:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        self.base = np.zeros((self.height, self.width, 3), dtype = np.uint8)
        
    def generate_canvas(self):
        if get_color(self.color) == None:
            self.base[:] = [*get_color(self.color)]
            return self
        else:
            return "Error! Cannot generate canvas due to unspecified color."

    def add_shape(self, x_start, x_end, y_start, y_end, color):
        self.base[y_start:y_end, x_start:x_end] = color

    def make_image(self, image_path):
        img = Image.fromarray(self.base, "RGB")
        img.save(image_path)

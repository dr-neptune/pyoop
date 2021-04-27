class Canvas:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        
    def generate_canvas(self):
        base = np.zeros((self.height, self.width, 3), dtype = np.uint8)
        if self.color == "black":
            base[:] = [0, 0, 0]
            return base
        elif self.color == "white":
            base[:] = [255, 255, 255]
            return base
        else:
            return "Error! Cannot generate canvas due to unspecified color (not black/white)"

    def make_image(image_path):
        pass

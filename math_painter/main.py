from color_dict import colors_dict

canvas = Canvas(1000, 1000, "black")
print(canvas.generate_canvas())

sq = Square(100, 100, 50, "green", canvas)
rect = Rectangle(100, 100, 150, 400, "blue", canvas)

print(sq)
print(rect)

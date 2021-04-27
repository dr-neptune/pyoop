from canvas import Canvas
from shape import Square, Rectangle
from color_dict import *
from webbrowser import open
from os import path

# enter canvas information
c_h = int(input("Enter canvas height (px):\n"))
c_w = int(input("Enter canvas width (px):\n"))
c_c = input("Enter the canvas color:\n")

canvas = Canvas(c_h, c_w, c_c)
canvas.generate_canvas()

# repeat the shape input prompt until quit is entered
def prompt(canvas):
    def draw_loop(shape = ""):
        global canvas
        if not shape in ["r", "s", "q"]:
            print(f"Error: Unknown shape: {shape}")
            return
        if shape == "q":
            filename_out = input("Please enter a filename for your masterpiece (example: album_cover (.png not required)):\n")
            filename_out = filename_out + ".png"
            canvas.make_image(filename_out)
            open("file://" + path.realpath(filename_out))
            print(f"Be sure to check out your art! {filename_out}")
            return
        else:
            s_color = input("What color is your shape?\n")
            x_coord = int(input("Enter the x coordinate of the upper left corner of your shape:\n"))
            y_coord = int(input("Enter the y coordinate of the upper left corner of your shape:\n"))
            s_width = int(input("Enter the width of your shape:\n"))
            if shape == "r":
                s_height = int(input("Enter the height of your rectangle:\n"))
                rect = Rectangle(x_coord, y_coord, s_height, s_width, s_color, canvas)
                canvas = rect.draw(canvas)
            else: # shape is s
                square = Square(x_coord, y_coord, s_width, s_color, canvas)
                canvas = square.draw(canvas)
        shape_input = input("What would you like to draw? (square (s), rectangle (r), quit (q)):\n")
        draw_loop(shape_input)
    shape_input = input("What would you like to draw? (square (s), rectangle (r), quit (q)):\n")
    draw_loop(shape_input)

prompt(canvas)

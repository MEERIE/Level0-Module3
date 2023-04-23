import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
# Returns a random color!
    t = turtle.Turtle()
    color_choice = simpledialog.askstring("Pen Color", "Enter a color for the pen (or press enter for random color): ")

    # Use an if/else statement to set the pen color that the user requested
    if color_choice:
        t.pencolor(color_choice)
    else:
        t.pencolor(get_random_color())

# Create a new Turtle
t = turtle.Turtle()

window = turtle.Screen()
window.bgcolor('white')

while True:
    # Make the turtle draw a shape
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

    # Set the pen width to 10
    t.pensize(10)
    break
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

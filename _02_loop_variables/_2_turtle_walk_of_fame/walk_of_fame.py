import turtle

if __name__ == '__main__':
    green = turtle.Turtle()
    green.shape('turtle')
    green.color('blue', 'green')
    green.speed(100)

    # TODO 1) Set the X position of the turtle so that it starts on the left.
    green.penup()
    green.setx(-400)
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.

    for i in range(5):
        for i in range(5):
            green.pendown()
            green.forward(30)
            green.right(144)
            green.penup()
        green.forward(100)
    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

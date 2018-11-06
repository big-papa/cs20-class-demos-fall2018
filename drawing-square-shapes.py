import turtle

def draw_square(a_turtle, side_length):
    """Draws a square with the turtle you pass in, with side lengths (given as integers)."""
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)

def draw_inner_squares(some_turtle, inner_square_length, boundary_length):
    """Draws two squares, with one inside the other.
        Takes in a turtle, the side length of the inner square, and the
        amount of space between the inner and outer squares."""
    draw_square(some_turtle, inner_square_length)
    some_turtle.penup()
    some_turtle.backward(boundary_length)
    some_turtle.right(90)
    some_turtle.forward(boundary_length)
    some_turtle.left(90)
    some_turtle.pendown()
    draw_square(some_turtle, inner_square_length + 2*boundary_length)

def draw_square_from_center(my_turtle, side_length):
    """Draws a square from the center coordinate of the square.
       Ends in the same location as it starts, facing the same way."""
    my_turtle.penup()
    for counter in range(2):
        my_turtle.right(90)
        my_turtle.forward(side_length/2)
    my_turtle.right(180)
    my_turtle.pendown()
    draw_square(my_turtle, side_length)
    my_turtle.penup()
    for counter in range(2):
        my_turtle.forward(side_length/2)
        my_turtle.left(90)
    my_turtle.left(180)
    my_turtle.pendown()

def draw_square_logo(some_turtle, side_length):
    """Draws a square logo, starting from the center point."""
    draw_square_from_center(some_turtle, side_length)
    some_turtle.left(45)
    draw_square_from_center(some_turtle, side_length)

window = turtle.Screen()

morgan = turtle.Turtle()
morgan.pensize(4)
morgan.color("red")

draw_square_logo(morgan, 100)

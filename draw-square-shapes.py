import turtle

def draw_square(some_turtle, side_length):
    """Draws a square with the given turtle, with each side being side_length long."""
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_inner_square(a_turtle, inner_square_length, buffer_size):
    """Draws an inner and outer square, with buffer_size space between them."""
    draw_square(a_turtle, inner_square_length)
    a_turtle.penup()
    a_turtle.backward(buffer_size)
    a_turtle.right(90)
    a_turtle.forward(buffer_size)
    a_turtle.left(90)
    a_turtle.pendown()
    draw_square(a_turtle, inner_square_length + 2*buffer_size)

def draw_square_from_center(my_turtle, side_length):
    """Draws a square, starts and ends at the center point."""
    my_turtle.penup()
    my_turtle.backward(side_length/2)
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.left(90)
    my_turtle.pendown()
    draw_square(my_turtle, side_length)
    my_turtle.penup()
    my_turtle.forward(side_length/2)
    my_turtle.left(90)
    my_turtle.forward(side_length/2)
    my_turtle.right(90)

def draw_logo(some_turtle, side_length):
    """Draws two overlapping squares, with one tilted by 45 degrees."""
    draw_square_from_center(some_turtle, side_length)
    some_turtle.left(45)
    draw_square_from_center(some_turtle, side_length)

screen = turtle.Screen()

blake = turtle.Turtle()
blake.color("blue")
blake.pensize(4)

draw_logo(blake, 200)
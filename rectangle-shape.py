import turtle

def draw_rectangle(some_turtle, length, width):
    """Draws a rectangle with the given turtle. Draws the long
        side first, then the shorter side. Ends facing same
        way as it started."""
    for counter in range(2):
        some_turtle.forward(length)
        some_turtle.left(90)
        some_turtle.forward(width)
        some_turtle.left(90)

canvas = turtle.Screen()
omar = turtle.Turtle()
omar.pensize(4)
omar.color("blue")

for rectangle in range(4):
    draw_rectangle(omar, 200, 70)
    omar.left(90)

import turtle

def draw_rectangle(some_turtle, length, width):
    """Draws a rectangle with the given turtle, with the long side being length,
        and the short side being width. Long side is drawn first."""
    for counter in range(2):
        some_turtle.forward(length)
        some_turtle.left(90)
        some_turtle.forward(width)
        some_turtle.left(90)

canvas = turtle.Screen()

morgan = turtle.Turtle()
morgan.color("red")
morgan.pensize(4)

for counter in range(4):
    draw_rectangle(morgan, 150, 75)
    morgan.left(90)

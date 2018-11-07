import turtle

def draw_filled_square(some_turtle, rgb_color, size):
    """Draws a filled in square, with a particular color."""
    some_turtle.color(rgb_color)
    some_turtle.begin_fill()
    for side in range(4):
        some_turtle.forward(size)
        some_turtle.left(90)
    some_turtle.end_fill()
    some_turtle.forward(size)

screen = turtle.Screen()
screen.colormode(255)

pen = turtle.Turtle()
pen.speed(0)

for red_amount in range(0, 255, 25):
    pen.penup()
    pen.goto(-300, red_amount)
    pen.pendown()
    for green_amount in range(0, 255, 25):
        draw_filled_square(pen, (red_amount, green_amount, 0), 25)

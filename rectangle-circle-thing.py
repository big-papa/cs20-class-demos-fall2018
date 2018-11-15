import turtle

def draw_rectangle(some_turtle, length, width):
    """Draws a rectangle, ending in the same location you started."""
    for counter in range(2):
        some_turtle.forward(length)
        some_turtle.left(90)
        some_turtle.forward(width)
        some_turtle.left(90)

def draw_rectangle_cicle_thing(a_turtle, number_of_sides, length, width):
    """Draws a bunch of rectangles to make a circle-ish shape."""
    for rectangle in range(number_of_sides):
        draw_rectangle(a_turtle, length, width)
        a_turtle.left(90)
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.left(360 / number_of_sides)

window = turtle.Screen()
therill = turtle.Turtle()
therill.pensize(4)
therill.speed(0)

draw_rectangle_cicle_thing(therill, 6, 150, 50)


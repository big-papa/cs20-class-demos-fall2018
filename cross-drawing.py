import turtle

def draw_cross(some_turtle, side_length):
    for counter in range(4):
        for side in range(2):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.forward(side_length)
        some_turtle.right(90)


canvas = turtle.Screen()

aaron = turtle.Turtle()
aaron.pensize(4)

robbie = turtle.Turtle()
robbie.color("blue")
robbie.pensize(3)

draw_cross(aaron, 75)
draw_cross(robbie, 200)




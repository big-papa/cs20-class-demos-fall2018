import turtle

def draw_cross(some_turtle, side_length):
    for counter in range(4):
        for side in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.right(180)

canvas = turtle.Screen()

mamun = turtle.Turtle()
mamun.color("blue")
mamun.pensize(4)

jenna = turtle.Turtle()
jenna.color("purple")
jenna.pensize(6)

draw_cross(mamun, 75)
draw_cross(jenna, 200)





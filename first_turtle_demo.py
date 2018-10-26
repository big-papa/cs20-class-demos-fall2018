import turtle
import easygui_qt as easy

shapes = easy.get_integer("How many shapes should we draw?")

canvas = turtle.Screen()
canvas.bgcolor("yellow")

ashton = turtle.Turtle()
ashton.color("blue")
ashton.shape("turtle")
ashton.pensize(4)
ashton.speed(0)

for number_of_shapes in range(shapes):
    for counter in range(4):
        ashton.forward(100)
        ashton.left(90)
    ashton.left(360/shapes)

import turtle
import easygui_qt as easy

the_window = turtle.Screen()
the_window.bgcolor("lightgreen")

the_color = easy.get_string("What color should the shape be?")
shapes = easy.get_integer("How many shapes should there be?")

shiloh = turtle.Turtle()
shiloh.color(the_color)
shiloh.shape("turtle")
shiloh.pensize(4)
shiloh.speed(0)

for number_of_shapes in range(shapes):
    for counter in range(4):
        shiloh.forward(100)
        shiloh.left(90)
    shiloh.left(360/shapes)

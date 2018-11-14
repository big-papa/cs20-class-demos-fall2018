import turtle
import easygui_qt as easy

the_color = easy.get_color_rgb()

window = turtle.Screen()
window.colormode(255)

bob = turtle.Turtle()
bob.color(the_color)
bob.pensize(10)

bob.forward(100)


import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

matt = turtle.Turtle()
matt.shape("turtle")
matt.color("blue")
matt.pensize(4)

morgan = turtle.Turtle()
morgan.shape("turtle")
morgan.color("red")
morgan.pensize(7)

for some_color in ["red", "blue", "yellow", "pink"]:
    morgan.color(some_color)
    morgan.right(90)
    morgan.forward(100)

# matt draws a triangle
for counter in range(3):
    matt.forward(200)
    matt.left(120)

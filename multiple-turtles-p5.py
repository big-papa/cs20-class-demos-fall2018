import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

omar = turtle.Turtle()
omar.shape("turtle")
omar.color("blue")
omar.pensize(5)
omar.speed(8)

issing = turtle.Turtle()
issing.shape("turtle")
issing.color("purple")
issing.pensize(10)

issing.backward(100)
issing.right(45)

for counter in range(3):
    omar.forward(200)
    omar.left(120)

for some_color in ["yellow", "blue", "red", "orange"]:
    issing.color(some_color)
    issing.forward(200)
    issing.right(90)

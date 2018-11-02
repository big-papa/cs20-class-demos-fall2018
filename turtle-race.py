# turtle race

import turtle
import random

#define constants
FINISH_LINE = 250

#setup the screen
window = turtle.Screen()

#setup the turtles
josh = turtle.Turtle()
josh.shape("turtle")
josh.color("red")
josh.penup()

steven = turtle.Turtle()
steven.shape("turtle")
steven.color("blue")
steven.penup()

#draw the finish line
ref = turtle.Turtle()
ref.penup()
ref.goto(FINISH_LINE, 75)
ref.pendown()
ref.goto(FINISH_LINE, -75)
ref.hideturtle()

#send turtles to the starting line
josh.goto(-250, 50)
steven.goto(-250, -50)

#do the actual race!
while josh.xcor() < FINISH_LINE and steven.xcor() < FINISH_LINE:
    josh.forward(random.randrange(1, 10))
    steven.forward(random.randrange(1, 10))

#print out a victory message
if josh.xcor() > steven.xcor():
    josh.write("Josh for the win!!", True, align="right",  font=("Arial", 24, "normal"))

elif steven.xcor() > josh.xcor():
    steven.write("Steven for the win!!", True, align="right",  font=("Arial", 24, "normal"))

else:
    steven.write("Everybody wins!!", True, align="right",  font=("Arial", 24, "normal"))
    josh.write("Everybody wins!!", True, align="right",  font=("Arial", 24, "normal"))
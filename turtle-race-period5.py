# Turtle Race
# Dan Schellenberg
# Nov 2, 2018

import turtle
import random

FINISH_LINE = 250

#setup screen
window = turtle.Screen()
window.bgcolor("red")

#setup turtles
ben = turtle.Turtle()
ben.color("pink")
ben.shape("turtle")
ben.penup()

afaq = turtle.Turtle()
afaq.color("yellow")
afaq.shape("turtle")
afaq.penup()

#draw the finish line
ref = turtle.Turtle()
ref.pensize(2)
ref.penup()
ref.goto(FINISH_LINE, 150)
ref.pendown()
ref.goto(FINISH_LINE, -150)
ref.hideturtle()

# send turtles to starting line
ben.goto(-300, 100)
afaq.goto(-300, -100)

while ben.xcor() < FINISH_LINE and afaq.xcor() < FINISH_LINE:
    ben_speed = random.randrange(1, 8) #5
    afaq_speed = random.randrange(1, 8) #4
    
    ben.forward(ben_speed)
    afaq.forward(afaq_speed)

if ben.xcor() > afaq.xcor():
    ben.write("Ben for the win!", move=False, align="right", font=("Arial", 24, "normal"))

elif afaq.xcor() > ben.xcor():
    afaq.write("Afaq for the win!", move=False, align="right", font=("Arial", 24, "normal"))

else:
    ben.write("Tie!", move=False, align="right", font=("Arial", 24, "normal"))
    afaq.write("Tie!", move=False, align="right", font=("Arial", 24, "normal"))
import microbit
import turtle
import sys

canvas = turtle.Screen()
canvas.bgcolor("red")

aaron = turtle.Turtle()
aaron.color("blue")
aaron.pensize(4)
aaron.shape("turtle")

while True:
    #draw a triangle if microbit button a is pressed
    if microbit.button_a.is_pressed():
        for counter in range(3):
            aaron.forward(200)
            aaron.left(120)

    #draw a pentagon if microbit button a is pressed
    if microbit.button_b.is_pressed():
        for counter in range(5):
            aaron.forward(200)
            aaron.left(360/5)
            
    #quit if flipped over
    if microbit.accelerometer.get_z() > 900:
        print("quitting!")
        sys.exit()
        
    if microbit.accelerometer.get_x() > 200:
        print("right")
        aaron.right(5)
    
    if microbit.accelerometer.get_x() < -200:
        print("left")
        aaron.left(5)
        
    if microbit.accelerometer.get_y() < -200:
        print("forward")
        aaron.forward(10)
    
    if microbit.accelerometer.get_y() > 200:
        print("backward")
        aaron.backward(10)

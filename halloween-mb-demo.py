import microbit
import time
import turtle
import sys

window = turtle.Screen()
quinn = turtle.Turtle()

while True:
    if microbit.button_a.was_pressed():
        #draw a triangle
        for counter in range(3):
            quinn.forward(200)
            quinn.left(120)
            
    if microbit.button_b.was_pressed():
        #draw a square
        for counter in range(4):
            quinn.forward(200)
            quinn.left(90)
    
    if microbit.accelerometer.get_z() > 800:
        # if flipped, exit
        sys.exit()
        
    # if tilted forward, move forward
    if microbit.accelerometer.get_y() < -200:
        quinn.forward(5)
    
    # if tilted backward, move backward
    if microbit.accelerometer.get_y() > 200:
        quinn.backward(5)
    
    # if tilted left, turn left
    if microbit.accelerometer.get_x() < -200:
        quinn.left(5)
    
    # if tilted right, turn right
    if microbit.accelerometer.get_x() > 200:
        quinn.right(5)
    
        

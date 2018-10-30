import microbit
import time
import turtle

window = turtle.Screen()
tim = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()
    if x > 200:
        print("Right")
        tim.forward(5)
    elif x < -200:
        print("Left")
        tim.backward(5)
    else:
        print("Not Tilted")
    time.sleep(0.1)
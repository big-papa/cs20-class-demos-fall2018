import turtle
import random

def is_still_in_screen(the_window, the_turtle):
    right_edge = the_window.window_width() / 2
    left_edge = -(the_window.window_width() / 2)
    top_edge = the_window.window_height() / 2
    bottom_edge = -(the_window.window_height() / 2)
    
    turtle_x = the_turtle.xcor()
    turtle_y = the_turtle.ycor()
    
    still_in = True
    if turtle_x > right_edge or turtle_x < left_edge:
        still_in = False
    if turtle_y > top_edge or turtle_y < bottom_edge:
        still_in = False
    
    return still_in


canvas = turtle.Screen()

zach = turtle.Turtle()
zach.color("blue")
zach.shape("turtle")

while is_still_in_screen(canvas, zach):
    coin = random.randrange(2)
    if coin == 0: #heads
        zach.left(90)
    else:         #tails
        zach.right(90)
    
    zach.forward(50)
    
print("All done")
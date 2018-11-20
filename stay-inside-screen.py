import turtle
import random

def in_screen(a_window, a_turtle):
    right_edge = a_window.window_width() / 2
    left_edge = -(a_window.window_width() / 2)
    top_edge = a_window.window_height() / 2
    bottom_edge = -(a_window.window_height() / 2)
    
    x = a_turtle.xcor()
    y = a_turtle.ycor()
    
    if x > right_edge or x < left_edge:
        return False
    elif y > top_edge or y < bottom_edge:
        return False
    else:
        return True
    

screen = turtle.Screen()

brody = turtle.Turtle()
brody.color("blue")
brody.shape("turtle")
brody.speed(0)
brody.pensize(3)

while in_screen(screen, brody):
    brody.forward(25)
    coin = random.randrange(0, 2)
    if coin == 0:   #tails
        brody.left(120)
    else:
        brody.right(120)

print("All done!")
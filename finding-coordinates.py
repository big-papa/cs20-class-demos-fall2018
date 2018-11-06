import turtle

def print_stuff(x, y):
    print(x, y)

window = turtle.Screen()
ben = turtle.Turtle()


window.onclick(print_stuff)
window.listen()
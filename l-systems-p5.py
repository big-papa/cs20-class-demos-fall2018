import turtle

def apply_rules(letter):
    """Apply rules to a single letter, and return the result."""
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    else:
        return letter

def process_string(original_string):
    """Apply rules to every letter in a string, and return the result."""
    next_string = ""
    for letter in original_string:
        next_string = next_string + apply_rules(letter)
    return next_string

def create_l_system(axiom, number_of_iterations):
    """Begin with the axiom, and apply the rules number_of_iterations times."""
    ending_string = axiom
    for counter in range(number_of_iterations):
        ending_string = process_string(ending_string)
    return ending_string

instructions = create_l_system("FXF--FF--FF", 7)

canvas = turtle.Screen()
canvas.tracer(2)
tanzeel = turtle.Turtle()
tanzeel.speed(0)
tanzeel.color("red")
tanzeel.pensize(3)

tanzeel.penup()
tanzeel.goto(-500, -300)
tanzeel.pendown()

for task in instructions:
    if task == "F":
        tanzeel.forward(3)
    elif task == "-":
        tanzeel.left(60)
        tanzeel.color("red")
    elif task == "+":
        tanzeel.right(60)
        tanzeel.color("blue")